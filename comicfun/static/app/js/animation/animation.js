$(function () {
    // 播放器初始化
    var player = new Player({
        id: 'player-block',
        url: $('#player-block').attr('data-animation-url'),
        playbackRate: [0.5, 0.75, 1, 1.5, 2],
        defaultPlaybackRate: 1
    });

    // 书签功能
    var csrf = $('[name="csrfmiddlewaretoken"]').val();
    var bookmarkBtn = $('#bookmark');
    bookmarkBtn.click(function () {
        $.ajax({
            type: "GET",
            async: true,
            url: '/bookmark/add',
            headers: {
                'X-CSRFToken': csrf
            },
            dataType: "json",
            data: {
                content_type: 3,
                target_link: location.href,
                target_id: bookmarkBtn.attr('data-chapter-id')
            },
            success: function (msg) {
                popAlertMsg(msg.msg);
            },
            error: function () {
                popAlertMsg('出错了,请稍后再试 ╮( •́ω•̀ )╭');
            }
        });
    });

    // 切换季标签页
    var volumeTabs = $('.volume-tab a');
    var volumeContents = $('.volume-content');
    var volumeBtns = $('.volume-btn');

    var initChapterId = $('#init-chapter-id').val();
    if (initChapterId === 'None') {
        volumeContents.eq(0).show();
        volumeBtns.eq(0).removeClass('btn-outline-primary').addClass('btn-primary');
    } else {
        volumeBtns.each(function () {
            if ($(this).attr('data-chapter-id') === initChapterId) {
                $(this).removeClass('btn-outline-primary').addClass('btn-primary');
                var volumeContentNode = $(this).parent().parent().parent();
                volumeContentNode.show();
                var idx = volumeContentNode.attr('data-volume-idx');
                volumeTabs.removeClass('active');
                volumeTabs.eq(parseInt(idx)).addClass('active');
            }
        });
    }

    volumeTabs.click(function (e) {
        volumeTabs.removeClass('active');
        $(this).addClass('active');
        var idx = $(this).attr('data-volume-idx');

        volumeContents.hide();
        $('.volume-content[data-volume-idx=' + idx + ']').show();

        e.preventDefault();
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
