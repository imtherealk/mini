require(['jquery'], function($) {
    $(function(){
        $('#mini-form-unregister').submit(function(){
            return confirm("정말로 탈퇴하시겠습니까?");
        });
    });
});
