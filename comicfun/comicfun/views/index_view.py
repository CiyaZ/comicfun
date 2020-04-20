from django.shortcuts import render
from comicfun.models import AdCarousel, AdNews, Author, Artifact


def index(request):
    """首页"""

    # 轮播广告
    carousel_list = AdCarousel.objects.all().order_by('display_order')[:5]

    # 更新速递
    news_list = AdNews.objects.all().order_by('-create_time')[:6]

    # 热门作者
    author_list = Author.objects.all().order_by('-released_cnt')[:4]

    # 小说推荐
    novel_list = Artifact.objects.filter(content_type=1).order_by('-last_modified_time')[:4]

    # 漫画推荐
    comic_list = Artifact.objects.filter(content_type=2).order_by('-last_modified_time')[:4]

    # 动画推荐
    animation_list = Artifact.objects.filter(content_type=3).order_by('-last_modified_time')[:4]

    return render(request, 'index.html', {
        'carousel_list': carousel_list,
        'news_list': news_list,
        'author_list': author_list,
        'novel_list': novel_list,
        'comic_list': comic_list,
        'animation_list': animation_list
    })
