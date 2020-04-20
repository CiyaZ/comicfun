from django.shortcuts import render
from django.core.paginator import Paginator
from comicfun.models import ContentTag
from comicfun.utils.page_util import calc_page_btn_list


def novel_list_page(request):
    """分页显示小说列表"""
    content_tag_id = request.GET.get('tag_id')
    current_page = 1
    if request.GET.get('current_page') is not None:
        current_page = int(request.GET.get('current_page'))
    content_tag = ContentTag.objects.get(pk=content_tag_id)
    artifact_list = content_tag.artifact_set.all().filter(content_type=1).order_by('-last_modified_time')
    paginator = Paginator(artifact_list, 20)
    artifact_list_page = paginator.page(current_page)
    page_btn_list = calc_page_btn_list(paginator, current_page)
    return render(request, 'novel/novel_list.html', {
        'artifact_list_page': artifact_list_page,
        'page_btn_list': page_btn_list,
        'current_page': current_page,
        'page_size': 20,
        'content_tag_id': content_tag_id
    })
