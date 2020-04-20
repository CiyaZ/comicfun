$(function () {
    // 通用封页卡片跳转
    $('.cover-card .cover').click(function () {
        var navType = $(this).attr('data-nav-type');
        switch (navType) {
            case 'tag-novel':
                var id = $(this).attr('data-tag-id');
                location.href = '/novels?tag_id=' + id;
                break;
            case 'tag-comic':
                id = $(this).attr('data-tag-id');
                location.href = '/comics?tag_id=' + id;
                break;
            case 'tag-animation':
                id = $(this).attr('data-tag-id');
                location.href = '/animations?tag_id=' + id;
                break;
            case 'novel':
                id = $(this).attr('data-artifact-id');
                location.href = '/novels/' + id;
                break;
            case 'comic':
                id = $(this).attr('data-artifact-id');
                location.href = '/comics/' + id;
                break;
            case 'animation':
                id = $(this).attr('data-artifact-id');
                location.href = '/animations/' + id;
                break;
        }
    });
});