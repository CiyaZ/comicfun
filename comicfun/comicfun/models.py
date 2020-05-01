from django.contrib.auth.models import User
from django.db import models


class Conf(models.Model):
    """站点配置
    site_theme_color 主题背景颜色，十六进制RGB值，默认6f42c1
    site_background  主题16:9背景图，值为图片URL，默认无背景图片
    """
    conf_key_choices = (
        ('site_theme_color', 'site_theme_color 主题背景色'),
        ('site_background', 'site_background 主题背景图'),
    )
    conf_key = models.CharField(choices=conf_key_choices, max_length=255)
    conf_value = models.CharField(max_length=255)

    def __str__(self):
        return self.conf_key


class AdCarousel(models.Model):
    """首页轮播配置"""
    title = models.CharField(max_length=255, verbose_name='标题')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    img_url = models.URLField(verbose_name='轮播图链接')
    target_url = models.URLField(null=True, blank=True, verbose_name='跳转链接')
    create_time = models.DateTimeField(verbose_name='创建时间')

    def __str__(self):
        return self.title


class AdNews(models.Model):
    """首页全新发布板块"""
    txt = models.CharField(max_length=255, verbose_name='文字内容')
    target_url = models.URLField(null=True, blank=True, verbose_name='跳转链接')
    create_time = models.DateTimeField(verbose_name='创建时间')

    def __str__(self):
        return self.txt


class ContentTag(models.Model):
    """内容分类标签实体类"""
    content_type_choices = (
        (0, '空占位类型'),
        (1, '小说'),
        (2, '漫画'),
        (3, '动画'),
        (4, '游戏'),
        (5, '绘画图集'),
        (6, '素材资源'),
    )
    content_type = models.IntegerField(choices=content_type_choices, verbose_name='内容类型')
    name = models.CharField(max_length=20, verbose_name='标签名')
    tag_img_url = models.URLField(verbose_name='标签封面图片')

    def __str__(self):
        return self.get_content_type_display() + '区 ' + self.name


class DataTag(models.Model):
    """标签实体类"""
    key = models.CharField(max_length=20, verbose_name='标签键')
    name = models.CharField(max_length=20, verbose_name='标签名值')

    def __str__(self):
        return '[ ' + self.key + ' - ' + self.name + ' ]'


class Author(models.Model):
    """作者实体类"""
    sex_choices = (
        (0, '不明'),
        (1, '男'),
        (2, '女'),
        (3, '扶她'),
    )
    name = models.CharField(max_length=20, verbose_name='作者名')
    sex = models.IntegerField(default=0, choices=sex_choices, verbose_name='性别')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='作者简介')
    avatar_url = models.URLField(null=True, verbose_name='头像链接')
    released_cnt = models.IntegerField(default=0, verbose_name='收录作品数')

    def __str__(self):
        return self.name


class Artifact(models.Model):
    """小说、漫画、动画、游戏、原画图集、素材包的基础信息实体类"""
    # 内容类型 0空占位类型 1小说 2漫画 3动画 4游戏 5原画图集 6素材包
    content_type_choices = (
        (0, '空占位类型'),
        (1, '小说'),
        (2, '漫画'),
        (3, '动画'),
        (4, '游戏'),
        (5, '绘画图集'),
        (6, '素材资源'),
    )
    content_type = models.IntegerField(choices=content_type_choices, verbose_name='内容类型')
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=255, verbose_name='作品简介')
    authors = models.ManyToManyField(Author, verbose_name='关联作者')
    content_tags = models.ManyToManyField('ContentTag', blank=True, verbose_name='题材标签')
    data_tags = models.ManyToManyField('DataTag', blank=True, verbose_name='标签')
    create_time = models.DateTimeField(verbose_name='创建时间')
    last_modified_time = models.DateTimeField(verbose_name='最后修改时间')

    def __str__(self):
        return self.title


class Novel(models.Model):
    """小说实体类"""
    artifact = models.OneToOneField(Artifact, on_delete=models.CASCADE, verbose_name='关联Artifact')
    cover_img_url = models.URLField(null=True, blank=True, verbose_name='小说封面图片链接')
    download_link = models.URLField(null=True, blank=True, verbose_name='下载链接')
    is_completed = models.BooleanField(default=False, verbose_name='完结标志')

    def __str__(self):
        return self.artifact.title


class NovelVolume(models.Model):
    """小说卷实体类"""
    title = models.CharField(max_length=50, verbose_name='卷标题')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='卷简介')
    cover_img_url = models.URLField(null=True, blank=True, verbose_name='卷封面图片链接')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='归属小说作品')

    def __str__(self):
        return self.novel.artifact.title + ' ' + self.title


class NovelChapter(models.Model):
    """小说章实体类"""
    title = models.CharField(max_length=50, verbose_name='章标题')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间')
    last_modified_time = models.DateTimeField(verbose_name='最后修改时间')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    novel_volume = models.ForeignKey(NovelVolume, on_delete=models.CASCADE, verbose_name='归属小说卷')

    def __str__(self):
        return self.novel_volume.novel.artifact.title + ' ' + self.novel_volume.title + ' ' + self.title


class Comic(models.Model):
    """漫画实体类"""
    artifact = models.OneToOneField(Artifact, on_delete=models.CASCADE, verbose_name='关联Artifact')
    cover_img_url = models.URLField(null=True, blank=True, verbose_name='漫画封面图片链接')
    download_link = models.URLField(null=True, blank=True, verbose_name='下载链接')
    is_completed = models.BooleanField(default=False, verbose_name='完结标志')

    def __str__(self):
        return self.artifact.title


class ComicVolume(models.Model):
    """漫画卷实体类"""
    title = models.CharField(max_length=50, verbose_name='卷标题')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='卷简介')
    cover_img_url = models.URLField(null=True, blank=True, verbose_name='卷封面图片链接')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, verbose_name='归属漫画作品')

    def __str__(self):
        return self.comic.artifact.title + ' ' + self.title


class ComicChapter(models.Model):
    """漫画话实体类"""
    split_type_choices = (
        (1, '普通'),
        (2, '条漫'),
    )
    color_type_choices = (
        (1, '黑白'),
        (2, '圆珠笔蓝'),
        (3, '红蓝'),
        (4, '彩色'),
    )
    title = models.CharField(max_length=50, verbose_name='话标题')
    # 分镜类型 1普通 2条漫
    split_type = models.IntegerField(default=1, choices=split_type_choices, verbose_name='漫画类型')
    # 色彩类型 1黑白 2圆珠笔蓝 3红蓝 4彩色
    color_type = models.IntegerField(default=1, choices=color_type_choices, verbose_name='色彩类型')
    create_time = models.DateTimeField(verbose_name='创建时间')
    last_modified_time = models.DateTimeField(verbose_name='最后修改时间')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    comic_volume = models.ForeignKey(ComicVolume, on_delete=models.CASCADE, verbose_name='归属漫画卷')

    def __str__(self):
        return self.comic_volume.comic.artifact.title + ' ' + self.comic_volume.title + ' ' + self.title


class ComicPage(models.Model):
    """漫画页实体类"""
    img_url = models.URLField(verbose_name='图片链接')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    comic_chapter = models.ForeignKey(ComicChapter, on_delete=models.CASCADE, verbose_name='归属漫画话')

    def __str__(self):
        return self.comic_chapter.comic_volume.comic.artifact.title + ' ' + \
               self.comic_chapter.comic_volume.title + ' ' + \
               self.comic_chapter.title + ' [P' + str(self.display_order) + ']'


class Animation(models.Model):
    """动画实体类"""
    artifact = models.OneToOneField(Artifact, on_delete=models.CASCADE, verbose_name='关联Artifact')
    cover_img_url = models.URLField(null=True, blank=True, verbose_name='动画封面图片链接')
    is_completed = models.BooleanField(default=False, verbose_name='完结标志')

    def __str__(self):
        return self.artifact.title


class AnimationVolume(models.Model):
    """动画季实体类"""
    title = models.CharField(max_length=50, verbose_name='季标题')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='季简介')
    cover_img_url = models.URLField(null=True, blank=True, verbose_name='季封面图片链接')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    animation = models.ForeignKey(Animation, on_delete=models.CASCADE, verbose_name='归属动画作品')

    def __str__(self):
        return self.animation.artifact.title + ' ' + self.title


class AnimationChapter(models.Model):
    """动画话实体类"""
    title = models.CharField(max_length=50, verbose_name='话标题')
    content_url = models.URLField(verbose_name='动画视频存储链接')
    create_time = models.DateTimeField(verbose_name='创建时间')
    last_modified_time = models.DateTimeField(verbose_name='最后修改时间')
    display_order = models.IntegerField(default=0, verbose_name='显示顺序')
    animation_volume = models.ForeignKey(AnimationVolume, on_delete=models.CASCADE, verbose_name='归属动画季')

    def __str__(self):
        return self.animation_volume.animation.artifact.title + ' ' + self.animation_volume.title + ' ' + self.title


class BookMark(models.Model):
    """书签实体类"""
    content_type_choices = (
        (1, '小说'),
        (2, '漫画'),
        (3, '动画'),
    )
    content_type = models.IntegerField(choices=content_type_choices, verbose_name='内容类型')
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='关联用户')
    target_link = models.URLField(verbose_name='目标链接')
    novel_chapter = models.ForeignKey(
        NovelChapter, null=True, blank=True, on_delete=models.CASCADE, verbose_name='关联小说章')
    comic_page = models.ForeignKey(ComicPage, null=True, blank=True, on_delete=models.CASCADE, verbose_name='关联漫画页')
    animation_chapter = models.ForeignKey(
        AnimationChapter, null=True, blank=True, on_delete=models.CASCADE, verbose_name='关联动画话')
    create_time = models.DateTimeField(verbose_name='创建时间')
