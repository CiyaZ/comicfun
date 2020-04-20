import json
from django.shortcuts import render
from comicfun.models import ComicChapter


def comic_content_page(request, id):
    """漫画内页"""
    comic_chapter = ComicChapter.objects.filter(pk=id).first()
    # 上一话和下一话
    comic_volume = comic_chapter.comic_volume
    next_record_id = None
    pre_record_id = None
    next_record = comic_volume.comicchapter_set.all().filter(display_order__gt=comic_chapter.display_order).first()
    if next_record is not None:
        next_record_id = next_record.pk
    pre_record = comic_volume.comicchapter_set.all().filter(display_order__lt=comic_chapter.display_order) \
        .order_by("-display_order").first()
    if pre_record is not None:
        pre_record_id = pre_record.pk
    # 全部图片列表
    comic_pages = comic_chapter.comicpage_set.all().order_by("display_order")
    comic_page_links = []
    i = 1
    for comic_page in comic_pages:
        comic_page_links.append({
            'p': i,
            'url': comic_page.img_url
        })
        i += 1

    return render(request, 'comic/comic_content.html', {
        'comic_chapter': comic_chapter,
        'next_record_id': next_record_id,
        'pre_record_id': pre_record_id,
        'comic_page_links': json.dumps({
            'data': comic_page_links
        })
    })
