require(['jquery'], function($) {
    $(function(){
        $('#mini-form-cmt-delete').submit(function(){
            return confirm("정말 삭제하시겠습니까?");
        });
    });
});