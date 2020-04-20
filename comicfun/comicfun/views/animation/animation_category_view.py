from django.shortcuts import render
from comicfun.models import ContentTag


def animation_category_page(request):
    """动画分类页"""
    content_tags = ContentTag.objects.filter(content_type=3)
    return render(request, 'animation/animation_category.html', {
        'content_tags': content_tags
    })
