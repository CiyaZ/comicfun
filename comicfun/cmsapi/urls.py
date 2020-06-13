from django.urls import path, re_path
from cmsapi.views import login_view, conf_view, content_tag_view

urlpatterns = [
    # 通用接口
    path('csrf', login_view.get_csrf),
    # 登录等出相关
    path('captcha', login_view.generate_captcha_info),
    path('login', login_view.do_login),
    path('loginInfo', login_view.get_login_info),
    path('logout', login_view.do_logout),
    # 站点配置信息
    path('confs', conf_view.get_conf_list),
    # 内容标签
    path('contentTags', content_tag_view.get_content_tag_list),
    re_path(r'^contentTags/(?P<pk>[0-9]+)$', content_tag_view.get_content_tag),
]
