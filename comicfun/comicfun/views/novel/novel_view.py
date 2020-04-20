from django.http import Http404
from django.shortcuts import render
from comicfun.models import Artifact


def novel_page(request, id):
    """小说页"""
    artifact_query_result = Artifact.objects.filter(pk=id)
    if len(artifact_query_result) < 1:
        return Http404()
    else:
        artifact = artifact_query_result.first()
        authors = artifact.authors.all()
        content_tags = artifact.content_tags.all()
        novel_volumes = artifact.novel.novelvolume_set.all().order_by('display_order')
        novel_chapters_arr = []
        for novel_volume in novel_volumes:
            novel_chapters = novel_volume.novelchapter_set.all().order_by('display_order')
            novel_chapters_arr.append(novel_chapters)
        return render(request, 'novel/novel.html', {
            'novel_artifact': artifact,
            'authors': authors,
            'content_tags': content_tags,
            'novel_volumes': novel_volumes,
            'novel_chapters_arr': novel_chapters_arr
        })
