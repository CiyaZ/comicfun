var isCheckingBegin = false;

$(function () {
    $('.form-control').blur(function () {
        if (isCheckingBegin) {
            check();
        }
    });
});

function check() {
    isCheckingBegin = true;
    $('.form-control').removeClass('is-invalid');

    var lastnameNode = $('#lastname');
    var firstnameNode = $('#firstname');
    var emailNode = $('#email');

    var lastnameErrNode = $('#lastname-err');
    var firstnameErrNode = $('#firstname-err');
    var emailErrNode = $('#email-err');

    if (lastnameNode.val().length > 150) {
        lastnameNode.addClass('is-invalid');
        lastnameErrNode.text('姓不能超过150个字符');
        return false;
    }

    if (firstnameNode.val().length > 150) {
        firstnameNode.addClass('is-invalid');
        firstnameErrNode.text('名不能超过30个字符');
        return false;
    }

    if (emailNode.val().length > 254) {
        emailNode.addClass('is-invalid');
        emailErrNode.text('邮箱不能超过254个字符');
        return false;
    }

    var emailRegex = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
    if (emailNode.val() !== '' && !emailRegex.test(emailNode.val())) {
        emailNode.addClass('is-invalid');
        emailErrNode.text('请输入正确的邮箱格式');
        return false;
    }

    return true;
}
