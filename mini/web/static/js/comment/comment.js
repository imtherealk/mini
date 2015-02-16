require(['jquery'], function($) {
    function addDeleteConfirmEvent(element){
        element.find('.mini-form-cmt-delete').submit(function(){
            return confirm("정말 삭제하시겠습니까?");
        });
    }
    $(function(){
        addDeleteConfirmEvent($(document));
        $('.mini-post').each(function() {
            var commentBox = $(this).find('.comment-box');
            $(this).find('.mini-comment').click(function(){
                commentBox.load(this.href, function() {
                    addDeleteConfirmEvent(commentBox);
                });
                commentBox.toggle();
                return false;
            });
        });
    });
    $(function(){
        $(function () {
        $('.comment-like').click(function(){
            $.post($(this).attr('href'),
                function(response, status){
                    alert(response);
                });
            return false;
        });
    });
    })
});
