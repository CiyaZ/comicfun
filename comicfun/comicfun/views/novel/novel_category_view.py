from django.shortcuts import render
from comicfun.models import ContentTag


def novel_category_page(request):
    """小说分类页"""
    content_tags = ContentTag.objects.filter(content_type=1)
    return render(request, 'novel/novel_category.html', {
        'content_tags': content_tags
    })
