from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.utils import timezone
from comicfun.models import BookMark, NovelChapter, ComicChapter, ComicPage, AnimationChapter
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def bookmark_page(request):
    """用户书签页面"""
    bookmarks = BookMark.objects.filter(auth_user=request.user)
    novel_bookmarks = []
    comic_bookmarks = []
    animation_bookmarks = []
    for bookmark in bookmarks:
        if bookmark.content_type == 1:
            novel_bookmarks.append(bookmark)
        elif bookmark.content_type == 2:
            comic_bookmarks.append(bookmark)
        elif bookmark.content_type == 3:
            animation_bookmarks.append(bookmark)
    return render(request, 'user/bookmark.html', {
        'novel_bookmarks': novel_bookmarks,
        'comic_bookmarks': comic_bookmarks,
        'animation_bookmarks': animation_bookmarks
    })


@login_required(login_url='/login')
def add_bookmark(request):
    """添加书签"""

    if request.user is None or not request.user.is_authenticated:
        return JsonResponse({
            'msg': '请先登录'
        })

    content_type = request.GET.get('content_type')
    target_link = request.GET.get('target_link')
    target_id = request.GET.get('target_id')

    if content_type is None or content_type == '':
        return JsonResponse({
            'msg': '参数校验错误'
        })

    if target_link is None or target_link == '':
        return JsonResponse({
            'msg': '参数校验错误'
        })

    if target_id is None or target_id == '':
        return JsonResponse({
            'msg': '参数校验错误'
        })

    bookmark = BookMark(auth_user=request.user, target_link=target_link, create_time=timezone.now())

    if content_type == '1':
        # 小说
        novel_chapter = NovelChapter.objects.get(pk=target_id)
        bookmark.content_type = 1
        bookmark.novel_chapter = novel_chapter
    elif content_type == '2':
        # 漫画 注意这里传的target_id是chapterId，target_idx是页码序号
        target_idx = request.GET.get('target_idx')
        if target_idx is None or target_idx == '':
            return JsonResponse({
                'msg': '参数校验错误'
            })
        target_idx = int(target_idx)
        comic_chapter = ComicChapter.objects.filter(pk=target_id).first()
        if comic_chapter is not None:
            comic_page = comic_chapter.comicpage_set.all().order_by("display_order")[target_idx]
            bookmark.content_type = 2
            bookmark.comic_page = comic_page
        else:
            return JsonResponse({
                'msg': '参数校验错误'
            })
    elif content_type == '3':
        # 动画
        animation_chapter = AnimationChapter.objects.get(pk=target_id)
        bookmark.content_type = 3
        bookmark.animation_chapter = animation_chapter

    bookmarks = BookMark.objects.filter(auth_user=request.user, target_link=target_link,
                                        content_type=bookmark.content_type,
                                        novel_chapter=bookmark.novel_chapter,
                                        comic_page=bookmark.comic_page,
                                        animation_chapter=bookmark.animation_chapter)
    if len(bookmarks) == 0:
        bookmark.save()

    return JsonResponse({
        'msg': '书签已添加'
    })


@login_required(login_url='/login')
def delete_bookmark(request):
    """删除书签"""
    bookmark_id = request.GET.get('id')
    bookmark = BookMark.objects.filter(pk=bookmark_id).first()
    if bookmark is not None:
        bookmark.delete()
    return HttpResponseRedirect('/bookmark')
