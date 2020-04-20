from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from captcha.models import CaptchaStore
from django.contrib.auth import authenticate, login, logout
from captcha.helpers import captcha_image_url


def login_page(request):
    """登录页"""
    captcha_key = CaptchaStore.generate_key()
    img_url = captcha_image_url(captcha_key)
    return render(request, 'login.html', {
        'captcha_key': captcha_key,
        'image_url': img_url
    })


def refresh_captcha(request):
    """更新验证码"""
    captcha_key = CaptchaStore.generate_key()
    img_url = captcha_image_url(captcha_key)
    return JsonResponse({
        'captcha_key': captcha_key,
        'image_url': img_url
    })


def do_login(request):
    """登录"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    captcha_value = request.POST.get('captcha-value')
    captcha_key = request.POST.get('captcha-key')

    if username is None or password is None or captcha_value is None or captcha_key is None:
        return HttpResponseBadRequest()

    # 验证码校验
    captcha = CaptchaStore.objects.get(hashkey=captcha_key)
    if captcha.response != captcha_value.lower():
        captcha_key = CaptchaStore.generate_key()
        img_url = captcha_image_url(captcha_key)
        return render(request, 'login.html', {
            'username': username,
            'err_msg': '验证码错误',
            'captcha_key': captcha_key,
            'image_url': img_url
        })

    # 登录校验
    user = authenticate(request, username=username, password=password)
    if user is None:
        captcha_key = CaptchaStore.generate_key()
        img_url = captcha_image_url(captcha_key)
        return render(request, 'login.html', {
            'username': username,
            'err_msg': '用户名或密码错误',
            'captcha_key': captcha_key,
            'image_url': img_url
        })

    login(request, user)
    return HttpResponseRedirect('/index')


def do_logout(request):
    """提交退出登录"""
    logout(request)
    return HttpResponseRedirect('/login')
