from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def account_info_page(request):
    """账号信息表单页"""
    return render(request, 'user/account_info.html', {})


@login_required(login_url='/login')
def do_update_account_info(request):
    """更新账号信息"""
    lastname = request.POST.get('lastname')
    firstname = request.POST.get('firstname')
    email = request.POST.get('email')

    # 表单校验
    if len(lastname) > 150:
        return HttpResponseBadRequest()
    if len(firstname) > 30:
        return HttpResponseBadRequest()
    if len(email) > 254:
        return HttpResponseBadRequest()
    print(firstname)
    user = User.objects.get(pk=request.user.pk)
    if lastname != '':
        user.last_name = lastname
    if firstname != '':
        user.first_name = firstname
    if email != '':
        user.email = email
    user.save()

    request.user = user

    return render(request, 'user/account_info.html', {
        'success_msg': '保存成功'
    })
