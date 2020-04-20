from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO
from comicfun.models import NovelChapter


def novel_content_page(request, id):
    """小说阅读页"""
    novel_chapter = NovelChapter.objects.filter(pk=id).first()
    # 上一章和下一章主键，用于翻页
    novel_volume = novel_chapter.novel_volume
    next_record_id = None
    pre_record_id = None
    next_record = novel_volume.novelchapter_set.all().filter(display_order__gt=novel_chapter.display_order).first()
    if next_record is not None:
        next_record_id = next_record.pk
    pre_record = novel_volume.novelchapter_set.all().filter(display_order__lt=novel_chapter.display_order).order_by("-display_order").first()
    if pre_record is not None:
        pre_record_id = pre_record.pk

    return render(request, 'novel/novel_content.html', {
        'novel_chapter': novel_chapter,
        'next_record_id': next_record_id,
        'pre_record_id': pre_record_id
    })


def generate_share_qrcode(request):
    """生成分享二维码"""
    url = request.GET.get('url')
    img = qrcode.make(url)
    buf = BytesIO()
    img.save(buf)
    return HttpResponse(buf.getvalue(), content_type='image/png')
