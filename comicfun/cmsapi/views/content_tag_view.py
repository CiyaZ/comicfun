from rest_framework.decorators import api_view, permission_classes
from cmsapi.util.response import APIResponse
from rest_framework.permissions import IsAdminUser
from comicfun.models import ContentTag
from cmsapi.serializers import ContentTagSerializer


@api_view(['GET', 'DELETE', 'POST'])
@permission_classes([IsAdminUser])
def get_content_tag_list(request):
    if request.method == 'GET':
        query_params = request.query_params.dict()
        para_content_type = None
        try:
            para_content_type = query_params['contentType']
        except KeyError:
            pass

        content_tags = ContentTag.objects.all()
        if para_content_type is not None:
            content_tags = content_tags.filter(content_type=para_content_type)

        resp_data = ContentTagSerializer(instance=content_tags, many=True)
        return APIResponse.success(resp_data.data)
    elif request.method == 'DELETE':
        query_params = request.query_params.dict()
        para_id = None
        try:
            para_id = query_params['id']
        except KeyError:
            return APIResponse.failure(None, '4000', '参数校验失败')

        content_tags = ContentTag.objects.filter(pk=para_id)
        if len(content_tags) == 0:
            return APIResponse.failure(None, '4001', '操作对象不存在')

        content_tag = content_tags[0]
        content_tag.delete()
        return APIResponse.success()
    elif request.method == 'POST':
        req_data = request.data
        content_type = req_data['contentType']
        name = req_data['name']
        tag_img_url = req_data['tagImageUrl']

        if content_type is None or content_type == '' or len(content_type) > 255 \
                or name is None or name == '' or len(name) > 255\
                or tag_img_url is None or tag_img_url == '' or len(tag_img_url) > 255:
            return APIResponse.failure(None, api_code='4000', api_msg='参数校验失败')

        content_tag = ContentTag(content_type=content_type, name=name, tag_img_url=tag_img_url)
        content_tag.save()
        return APIResponse.success()


@api_view(['GET', 'PUT'])
@permission_classes([IsAdminUser])
def get_content_tag(request, pk):
    if request.method == 'GET':
        content_tags = ContentTag.objects.filter(pk=pk)
        if len(content_tags) == 0:
            return APIResponse.failure({}, '4001', '操作对象不存在')
        content_tag = content_tags[0]
        return APIResponse.success(ContentTagSerializer(instance=content_tag).data)
    elif request.method == 'PUT':
        req_data = request.data
        content_tag_id = req_data['id']
        content_type = req_data['contentType']
        name = req_data['name']
        tag_img_url = req_data['tagImageUrl']

        if content_tag_id is None or content_tag_id == '' or content_type is None or content_type == '' \
                or name is None or name == '' or len(name) > 255 or tag_img_url is None or tag_img_url == '' or len(tag_img_url) > 255:
            return APIResponse.failure(None, api_code='4000', api_msg='参数校验失败')

        content_tags = ContentTag.objects.filter(pk=content_tag_id)
        if len(content_tags) == 0:
            return APIResponse.failure(None, '4001', '操作对象不存在')

        content_tag = content_tags[0]
        content_tag.content_type = int(content_type)
        content_tag.name = name
        content_tag.tag_img_url = tag_img_url
        content_tag.save()
        return APIResponse.success()
