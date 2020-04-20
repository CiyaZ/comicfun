from django.http import Http404
from django.shortcuts import render
from comicfun.models import Artifact, AnimationChapter


def animation_page(request, id):
    """动画页"""
    artifact_query_result = Artifact.objects.filter(pk=id)
    if len(artifact_query_result) < 1:
        return Http404()
    else:
        # 查询artifact
        artifact = artifact_query_result.first()
        # 查询作者
        authors = artifact.authors.all()
        # 查询归属分类
        content_tags = artifact.content_tags.all()
        # 查询季集列表信息
        animation_volumes = artifact.animation.animationvolume_set.all().order_by('display_order')
        animation_chapters_arr = []
        for animation_volume in animation_volumes:
            animation_chapters = animation_volume.animationchapter_set.all().order_by('display_order')
            animation_chapters_arr.append(animation_chapters)
        # 选集，参数不存在默认第一季第一集
        init_chapter_id = request.GET.get('chapter_id')
        if init_chapter_id is None or init_chapter_id == '':
            first_chapter = animation_chapters_arr[0].first()
            if first_chapter is not None:
                init_chapter_id = first_chapter.pk
        init_chapter = None
        if init_chapter_id is not None and init_chapter_id != '':
            init_chapter = AnimationChapter.objects.get(pk=init_chapter_id)
        return render(request, 'animation/animation.html', {
            'animation_artifact': artifact,
            'authors': authors,
            'content_tags': content_tags,
            'animation_volumes': animation_volumes,
            'animation_chapters_arr': animation_chapters_arr,
            'init_chapter': init_chapter
        })
