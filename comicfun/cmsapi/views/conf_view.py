from rest_framework.decorators import api_view, permission_classes
from cmsapi.util.response import APIResponse
from rest_framework.permissions import IsAdminUser
from comicfun.models import Conf
from cmsapi.serializers import ConfSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def get_conf_list(request):
    if request.method == 'GET':
        confs = Conf.objects.all()
        resp_data = ConfSerializer(instance=confs, many=True)
        return APIResponse.success(resp_data.data)
    elif request.method == 'POST':
        req_data = request.data
        conf_value_site_theme_color = req_data['mainColor']
        conf_value_site_background = req_data['bgImageUrl']

        if conf_value_site_theme_color is not None and conf_value_site_theme_color != '':
            conf_site_theme_color_queryset = Conf.objects.filter(conf_key='site_theme_color')
            if len(conf_site_theme_color_queryset) > 0:
                conf_site_theme_color = conf_site_theme_color_queryset[0]
                conf_site_theme_color.conf_value = conf_value_site_theme_color
                conf_site_theme_color.save()
            else:
                conf = Conf(conf_key='site_theme_color', conf_value=conf_value_site_theme_color)
                conf.save()

        if conf_value_site_background is not None and conf_value_site_background != '':
            conf_site_background_queryset = Conf.objects.filter(conf_key='site_background')
            if len(conf_site_background_queryset) > 0:
                conf_site_background = conf_site_background_queryset[0]
                conf_site_background.conf_value = conf_value_site_background
                conf_site_background.save()
            else:
                conf = Conf(conf_key='site_background', conf_value=conf_value_site_background)
                conf.save()

        return APIResponse.success()
