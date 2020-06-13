from django.core.exceptions import ObjectDoesNotExist
from django.middleware import csrf
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from cmsapi.util.response import APIResponse


@api_view(['GET'])
def generate_captcha_info(request):
    """生成验证码"""
    captcha_key = CaptchaStore.generate_key()
    img_url = captcha_image_url(captcha_key)
    return APIResponse.success({
        'captcha_key': captcha_key,
        'img_url': img_url
    })


@api_view(['GET'])
def get_csrf(request):
    csrf_token = csrf.get_token(request)
    return APIResponse.success({
        'csrf_token': csrf_token
    })


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_login_info(request):
    if request.user.is_authenticated:
        current_user = request.user
        return APIResponse.success({
            'username': current_user.username,
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'is_staff': current_user.is_staff
        })
    else:
        return APIResponse.failure(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def do_login(request):
    """确认登录"""
    req_data = request.data
    username = req_data['username']
    password = req_data['password']
    captcha_key = req_data['captchaKey']
    captcha_value = req_data['captchaValue']

    # 校验
    if username is None or username == '' \
            or password is None or password == '' \
            or captcha_key is None or captcha_key == '' \
            or captcha_value is None or captcha_value == '':
        return APIResponse.failure(None, api_code='4000', api_msg='参数校验失败')

    # 验证码校验
    captcha = CaptchaStore.objects.get(hashkey=captcha_key)
    if captcha.response != captcha_value.lower():
        return APIResponse.failure(api_code='4001', api_msg='验证码校验失败')

    # 登录校验
    user = authenticate(request, username=username, password=password)
    if user is None:
        return APIResponse.failure(api_code='4002', api_msg='用户名或密码错误')
    if not user.is_staff:
        return APIResponse.failure(api_code='4003', api_msg='用户无后台维护权限')
    login(request, user)

    # 生成token（funcms使用sessionId，客户端使用token）
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    token = Token.objects.create(user=user)

    return APIResponse.success({
        'token': token.key
    })


@api_view(['POST'])
@permission_classes([IsAdminUser])
def do_logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    logout(request)
    return APIResponse.success()
