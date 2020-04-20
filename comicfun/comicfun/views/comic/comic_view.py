from django.http import Http404
from django.shortcuts import render
from comicfun.models import Artifact


def comic_page(request, id):
    """漫画页"""
    artifact_query_result = Artifact.objects.filter(pk=id)
    if len(artifact_query_result) < 1:
        return Http404()
    else:
        artifact = artifact_query_result.first()
        authors = artifact.authors.all()
        content_tags = artifact.content_tags.all()
        comic_volumes = artifact.comic.comicvolume_set.all().order_by('display_order')
        comic_chapters_arr = []
        for comic_volume in comic_volumes:
            comic_chapters = comic_volume.comicchapter_set.all().order_by('display_order')
            comic_chapters_arr.append(comic_chapters)
        return render(request, 'comic/comic.html', {
            'comic_artifact': artifact,
            'authors': authors,
            'content_tags': content_tags,
            'comic_volumes': comic_volumes,
            'comic_chapters_arr': comic_chapters_arr
        })
