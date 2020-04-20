$(function () {

    // 初始化popover组件
    $('[data-toggle="tooltip"]').tooltip();

    $('.bookmark').click(function () {
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
                content_type: 1,
                target_link: location.href,
                target_id: $('#novel-chapter-id').val()

            },
            success: function (msg) {
                popAlertMsg(msg.msg);
            },
            error: function () {
                popAlertMsg('出错了,请稍后再试 ╮( •́ω•̀ )╭');
            }
        });
    });

    // 链接二维码功能
    $('#share-frame').attr('src', '/novels/content/share?url=' + encodeURI(location.href));

    $('#show-qrcode').click(function () {
        $('#modal').modal('show');
    });

    // 返回书页
    $('#nav-to-novel-page').click(function () {
        location.href = '/novels/' + $(this).attr('data-novel-id');
    });

    // 回到顶部
    $('#back-top').click(function () {
        $("body,html").animate({
            scrollTop: 0
        }, 800);
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


