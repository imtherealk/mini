require(['jquery'], function ($) {
    $(function () {
        $('.mini-form-post-delete').submit(function () {
            return confirm("정말 삭제하시겠습니까?");
        });
    });
    $(function () {
        $('.post-like').click(function(){
            $.post($(this).attr('href'),
                function(response, status){
                    alert(response);
                });
            return false;
        });
    });
});