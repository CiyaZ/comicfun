from comicfun.models import Conf


class ConfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site_conf = {
            'site_theme_color': '6f42c1',
            'site_background': None
        }
        conf_list = Conf.objects.all()
        for conf in conf_list:
            if conf.conf_key == 'site_theme_color' and conf.conf_value is not None and conf.conf_value != '':
                site_conf['site_theme_color'] = conf.conf_value
            if conf.conf_key == 'site_background' and conf.conf_value is not None and conf.conf_value != '':
                site_conf['site_background'] = conf.conf_value
        request.site_conf = site_conf

        response = self.get_response(request)
        return response
