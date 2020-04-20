from django.shortcuts import render
from comicfun.models import ContentTag


def comic_category_page(request):
    """漫画分类页"""
    content_tags = ContentTag.objects.filter(content_type=2)
    return render(request, 'comic/comic_category.html', {
        'content_tags': content_tags
    })
