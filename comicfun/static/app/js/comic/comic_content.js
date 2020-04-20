$(function () {
    // 初始化popover组件
    $('[data-toggle="tooltip"]').tooltip();

    // 漫画图页数据
    var comicPageLinks = JSON.parse($('#comic-page-links').val()).data;

    // 设置页面左上角页码显示框
    function setCurrentDisplayPage(i) {
        $('#current-page').text(i + 1);
    }

    // 初始化加载，根据location.hash值加载对应图片
    if (location.hash === '') {
        location.hash = '/1';
    }
    var pageIdx = parseInt(location.hash.slice(2)) - 1;
    var comicDisplay = $('#comic-display');
    comicDisplay.attr('src', comicPageLinks[pageIdx].url);
    setCurrentDisplayPage(pageIdx);

    // 判断鼠标位置设定左右触发
    var cursorAct = 'none';
    comicDisplay.mousemove(function (e) {
        var posX = e.offsetX;
        var posY = e.offsetY;
        var comicDisplayW = comicDisplay.width();
        var comicDisplayH = comicDisplay.height();
        var active_size = Math.floor(comicDisplayW / 2 - 10);

        if (posX >= 0 && posX <= active_size) {
            comicDisplay.css('cursor', 'url(/static/app/images/comic/cursor_left.png),auto');
            cursorAct = 'pre';
        } else if (posX >= comicDisplayW - active_size && posX <= comicDisplayW) {
            comicDisplay.css('cursor', 'url(/static/app/images/comic/cursor_right.png),auto');
            cursorAct = 'next';
        } else {
            comicDisplay.css('cursor', 'auto');
            cursorAct = 'none';
        }
        showToolbar();
    });

    comicDisplay.click(function () {
        switch (cursorAct) {
            case 'pre':
                toPrePage();
                break;
            case 'next':
                toNextPage();
                break;
            default:
                break;
        }
    });

    function toPrePage() {
        if (pageIdx !== 0) {
            pageIdx--;
            var url = comicPageLinks[pageIdx].url;
            comicDisplay.attr('src', url);
            location.hash = '/' + (pageIdx + 1);
            setCurrentDisplayPage(pageIdx);
        } else {
            popAlertMsg('已经是第一页了');
        }
    }

    function toNextPage() {
        if (pageIdx !== comicPageLinks.length - 1) {
            pageIdx++;
            var url = comicPageLinks[pageIdx].url;
            comicDisplay.attr('src', url);
            location.hash = '/' + (pageIdx + 1);
            setCurrentDisplayPage(pageIdx);
        } else {
            popAlertMsg('已经最后一页了');
        }
    }

    // 底部工具按钮组控制 左上角页码显示隐藏控制
    var toolbar = $('#toolbar-container');
    var pageInfo = $('#page-info-container');
    var fadeOutTimer = null;

    function showToolbar() {
        toolbar.fadeIn('slow');
        pageInfo.fadeIn('slow');
        clearInterval(fadeOutTimer);
        fadeOutTimer = setInterval(function () {
            if ($('#toolbar-container:hover').length <= 0) {
                hideToolbar();
            }
        }, 2000);
    }

    function hideToolbar() {
        toolbar.fadeOut('slow');
        pageInfo.fadeOut('slow');
    }

    var preChapterBtn = $('#pre-chapter');
    preChapterBtn.click(function () {
        var preChapterId = preChapterBtn.attr('data-nav-chapter-id');
        if (preChapterId !== 'None') {
            location.href = '/comics/content/' + preChapterId + '#/1';
        } else {
            popAlertMsg('已经是本卷第一话了');
        }
    });

    var nextChapterBtn = $('#next-chapter');
    nextChapterBtn.click(function () {
        var nextChapterId = nextChapterBtn.attr('data-nav-chapter-id');
        if (nextChapterId !== 'None') {
            location.href = '/comics/content/' + nextChapterId + '#/1';
        } else {
            popAlertMsg('已经是本卷最后一话了');
        }
    });

    $('#pre-page').click(toPrePage);
    $('#next-page').click(toNextPage);

    var backBtn = $('#back');
    backBtn.click(function () {
        var artifactId = backBtn.attr('data-nav-artifact-id');
        location.href = '/comics/' + artifactId;
    });

    var bookmarkBtn = $('#bookmark');
    bookmarkBtn.click(function () {
        var csrf = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: "GET",
            async: true,
            url: '/bookmark/add',
            headers: {
                'X-CSRFToken': csrf
            },
            dataType: "json",
            data: {
                content_type: 2,
                target_link: location.href,
                target_id: bookmarkBtn.attr('data-chapter-id'),
                target_idx: pageIdx
            },
            success: function (msg) {
                popAlertMsg(msg.msg);
            },
            error: function () {
                popAlertMsg('出错了,请稍后再试 ╮( •́ω•̀ )╭');
            }
        });
    });

    // 顶部警告提示功能
    var alertQueue = $('#alert-queue');

    function popAlertMsg(msg) {
        var alertNode = $('<div class="alert alert-comic"></div>');
        alertNode.text(msg);
        alertQueue.append(alertNode);
        alertNode.fadeIn('slow');
        setTimeout(function () {
            alertNode.fadeOut('slow', function () {
                alertNode.remove();
            });
        }, 2000);
    }
});