var isCheckingBegin = false;

$(function () {
    $('.form-control').blur(function () {
        if (isCheckingBegin) {
            check();
        }
    });

    var imgNode = $('#captcha-img');
    imgNode.click(function () {
        var csrf = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: "POST",
            async: true,
            url: '/login/captcha',
            headers: {
                'X-CSRFToken': csrf
            },
            dataType: "json",
            success: function (msg) {
                imgNode.attr('src', msg.image_url);
                $('#captcha-key').val(msg.captcha_key);
            }
        });
    });
});

function check() {
    isCheckingBegin = true;
    $('.form-control').removeClass('is-invalid');

    var usernameNode = $('#username');
    var passwordNode = $('#password');
    var captchaNode = $('#captcha');

    var usernameErrNode = $('#username-err');
    var passwordErrNode = $('#password-err');
    var captchaErrNode = $('#captcha-err');

    if (usernameNode.val() === '') {
        usernameNode.addClass('is-invalid');
        usernameErrNode.text('用户名不能为空');
        return false;
    }

    if (usernameNode.val().length > 20) {
        usernameNode.addClass('is-invalid');
        usernameErrNode.text('用户名不能超过20个字符');
        return false;
    }

    if (!/[a-z0-9]+/.test(usernameNode.val())) {
        usernameNode.addClass('is-invalid');
        usernameErrNode.text('用户名只能为小写字母和数字');
        return false;
    }

    if (passwordNode.val() === '') {
        passwordNode.addClass('is-invalid');
        passwordErrNode.text('密码不能为空');
        return false;
    }

    if (passwordNode.val().length > 20) {
        passwordNode.addClass('is-invalid');
        passwordErrNode.text('密码不能超过20个字符');
        return false;
    }

    if (captchaNode.val() === '') {
        captchaNode.addClass('is-invalid');
        captchaErrNode.text('验证码不能为空');
        return false;
    }

    return true;
}
