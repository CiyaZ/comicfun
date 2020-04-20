"""comicfun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from comicfun.views.login_view import login_page, do_login, refresh_captcha, do_logout
from comicfun.views.index_view import index
from comicfun.views.user.account_info_view import account_info_page, do_update_account_info
from comicfun.views.novel.novel_view import novel_page
from comicfun.views.novel.novel_content_view import novel_content_page, generate_share_qrcode
from comicfun.views.novel.novel_category_view import novel_category_page
from comicfun.views.novel.novel_list_view import novel_list_page
from comicfun.views.comic.comic_category_view import comic_category_page
from comicfun.views.comic.comic_list_view import comic_list_page
from comicfun.views.comic.comic_view import comic_page
from comicfun.views.comic.comic_content_view import comic_content_page
from comicfun.views.animation.animation_category_view import animation_category_page
from comicfun.views.animation.animation_list_view import animation_list_page
from comicfun.views.animation.animation_view import animation_page
from comicfun.views.user.bookmark_view import bookmark_page, add_bookmark, delete_bookmark
from comicfun.views.search_view import search_page

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index),
    path('index', index),
    path('search', search_page),
    # 登录相关
    path('login', login_page),
    path('login/submit', do_login),
    path('login/captcha', refresh_captcha),
    path('logout', do_logout),
    # user
    path('account', account_info_page),
    path('account/update', do_update_account_info),
    path('bookmark', bookmark_page),
    path('bookmark/add', add_bookmark),
    path('bookmark/delete', delete_bookmark),
    # 验证码路由
    path('captcha/', include('captcha.urls')),
    # 小说区
    path('novels/category', novel_category_page),
    path('novels', novel_list_page),
    re_path(r'^novels/(?P<id>[0-9]+)$', novel_page),
    re_path(r'^novels/content/(?P<id>[0-9]+)$', novel_content_page),
    path('novels/content/share', generate_share_qrcode),
    # 漫画区
    path('comics/category', comic_category_page),
    path('comics', comic_list_page),
    re_path(r'^comics/(?P<id>[0-9]+)$', comic_page),
    re_path(r'^comics/content/(?P<id>[0-9]+)$', comic_content_page),
    # 动画区
    path('animations/category', animation_category_page),
    path('animations', animation_list_page),
    re_path(r'^animations/(?P<id>[0-9]+)$', animation_page),
]
