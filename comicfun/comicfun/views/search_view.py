from django.shortcuts import render
from django.core.paginator import Paginator
from comicfun.models import Artifact
from comicfun.utils.page_util import calc_page_btn_list


def search_page(request):
    """搜索页面"""
    pattern = request.GET.get('pattern')
    current_page = 1
    if request.GET.get('current_page') is not None:
        current_page = int(request.GET.get('current_page'))

    # 模糊查询
    artifact_list = Artifact.objects.filter(title__contains=pattern) | Artifact.objects.filter(desc__contains=pattern)
    artifact_list.order_by('-last_modified_time')

    # 分页
    paginator = Paginator(artifact_list, 20)
    artifact_list_page = paginator.page(current_page)
    page_btn_list = calc_page_btn_list(paginator, current_page)

    return render(request, 'search.html', {
        'pattern': pattern,
        'artifact_list_page': artifact_list_page,
        'page_btn_list': page_btn_list,
        'current_page': current_page,
        'page_size': 20,
    })
