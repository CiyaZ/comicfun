from django.middleware import csrf
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from captcha.models import CaptchaStore
from django.contrib.auth import authenticate, login, logout
from captcha.helpers import captcha_image_url


@api_view(['GET'])
def generate_captcha_info(request):
    """生成验证码"""
    captcha_key = CaptchaStore.generate_key()
    img_url = captcha_image_url(captcha_key)
    return Response({
        'rspCode': '0',
        'rspMsg': '操作成功',
        'data': {
            'captcha_key': captcha_key,
            'img_url': img_url
        }
    })


@api_view(['GET'])
def get_csrf(request):
    csrf_token = csrf.get_token(request)
    return Response({
        'rspCode': '0',
        'rspMsg': '操作成功',
        'data': {
            'csrf_token': csrf_token
        }
    })


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_login_info(request):
    if request.user.is_authenticated:
        current_user = request.user
        return Response({
            'rspCode': '0',
            'rspMsg': '操作成功',
            'data': {
                'username': current_user.username,
                'email': current_user.email,
                'first_name': current_user.first_name,
                'last_name': current_user.last_name,
                'is_staff': current_user.is_staff
            }
        })
    else:
        return Response({}, status=status.HTTP_403_FORBIDDEN)


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
        return Response({
            'rspCode': '4000',
            'rspMsg': '参数校验失败',
            'data': None
        })

    # 验证码校验
    captcha = CaptchaStore.objects.get(hashkey=captcha_key)
    if captcha.response != captcha_value.lower():
        return Response({
            'rspCode': '4001',
            'rspMsg': '验证码校验失败',
            'data': None
        })

    # 登录校验
    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({
            'rspCode': '4002',
            'rspMsg': '用户名或密码错误',
            'data': None
        })
    if not user.is_staff:
        return Response({
            'rspCode': '4003',
            'rspMsg': '用户无后台维护权限',
            'data': None
        })
    login(request, user)

    return Response({
        'rspCode': '0',
        'rspMsg': '登录成功',
        'data': None
    })


@api_view(['POST'])
@permission_classes([IsAdminUser])
def do_logout(request):
    logout(request)
    return Response({
        'rspCode': '0',
        'rspMsg': '登出成功',
        'data': None
    })
