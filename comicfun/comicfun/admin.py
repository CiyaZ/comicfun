from django.contrib import admin
from comicfun.models import *


@admin.register(Conf)
class ConfAdmin(admin.ModelAdmin):
    list_display = ('conf_key', 'conf_value')
    search_fields = ['conf_key']


@admin.register(AdCarousel)
class AdCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'create_time')
    search_fields = ['title']


@admin.register(AdNews)
class AdNewsAdmin(admin.ModelAdmin):
    list_display = ('txt', 'target_url', 'create_time')
    search_fields = ['txt']


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_content_type_display', 'create_time', 'last_modified_time')
    search_fields = ['title']

    def get_content_type_display(self, obj):
        return obj.get_content_type_display()

    get_content_type_display.short_description = '内容类型'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'released_cnt')
    search_fields = ['name']


@admin.register(ContentTag)
class ContentTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


@admin.register(DataTag)
class DataTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'name')
    search_fields = ['key', 'name']


@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_artifact_title', 'is_completed')

    def get_artifact_title(self, obj):
        return obj.artifact.title

    get_artifact_title.short_description = 'Artifact标题'


@admin.register(NovelVolume)
class NovelVolumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'get_artifact_title')

    def get_artifact_title(self, obj):
        return obj.novel.artifact.title

    get_artifact_title.short_description = 'Artifact标题'


@admin.register(NovelChapter)
class NovelChapterAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'display_order', 'get_artifact_title', 'get_volume_title', 'create_time', 'last_modified_time')

    def get_artifact_title(self, obj):
        return obj.novel_volume.novel.artifact.title

    def get_volume_title(self, obj):
        return obj.novel_volume.title

    get_artifact_title.short_description = 'Artifact标题'
    get_volume_title.short_description = 'NovelVolume标题'


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_artifact_title', 'is_completed')

    def get_artifact_title(self, obj):
        return obj.artifact.title

    get_artifact_title.short_description = 'Artifact标题'


@admin.register(ComicVolume)
class ComicVolumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'get_artifact_title')

    def get_artifact_title(self, obj):
        return obj.comic.artifact.title

    get_artifact_title.short_description = 'Artifact标题'


@admin.register(ComicChapter)
class ComicChapterAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'display_order', 'get_artifact_title', 'get_volume_title', 'create_time', 'last_modified_time')

    def get_artifact_title(self, obj):
        return obj.comic_volume.comic.artifact.title

    def get_volume_title(self, obj):
        return obj.comic_volume.title

    get_artifact_title.short_description = 'Artifact标题'
    get_volume_title.short_description = 'ComicVolume标题'


@admin.register(ComicPage)
class ComicPageAdmin(admin.ModelAdmin):
    list_display = ('get_artifact_title', 'get_volume_title', 'get_chapter_title', 'display_order')

    def get_artifact_title(self, obj):
        return obj.comic_chapter.comic_volume.comic.artifact.title

    def get_volume_title(self, obj):
        return obj.comic_chapter.comic_volume.title

    def get_chapter_title(self, obj):
        return obj.comic_chapter.title

    get_artifact_title.short_description = 'Artifact标题'
    get_volume_title.short_description = 'ComicVolume标题'
    get_chapter_title.short_description = 'ComicChapter标题'


@admin.register(Animation)
class AnimationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_artifact_title', 'is_completed')

    def get_artifact_title(self, obj):
        return obj.artifact.title

    get_artifact_title.short_description = 'Artifact标题'


@admin.register(AnimationVolume)
class AnimationVolumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'get_artifact_title')

    def get_artifact_title(self, obj):
        return obj.animation.artifact.title

    get_artifact_title.short_description = 'Artifact标题'


@admin.register(AnimationChapter)
class AnimationChapterAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'display_order', 'get_artifact_title', 'get_volume_title', 'create_time', 'last_modified_time')

    def get_artifact_title(self, obj):
        return obj.animation_volume.animation.artifact.title

    def get_volume_title(self, obj):
        return obj.animation_volume.title

    get_artifact_title.short_description = 'Artifact标题'
    get_volume_title.short_description = 'AnimationVolume标题'
