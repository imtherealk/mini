require(['jquery'], function($) {
    function addDeleteConfirmEvent(element){
        element.find('.mini-form-cmt-delete').submit(function(){
            return confirm("정말 삭제하시겠습니까?");
        });
    }
    function addCommentLikeEvent(element){
        element.find('.each-comment').each(function() {
            var likes = $(this).find('.comment-like-count');
            $(this).find('.comment-like').click(function () {
                $.post(this.href, function (response, status) {
                    var json_response = $.parseJSON(response);
                    if (json_response.like_count != '0')
                        likes.text(json_response.like_count);
                    else
                        likes.text('');
                });
                return false;
            });
        })
    }
    $(function(){
        addDeleteConfirmEvent($(document));
        addCommentLikeEvent($(document));
        $('.mini-post').each(function() {
            var commentBox = $(this).find('.comment-box');
            $(this).find('.mini-comment').click(function(){
                commentBox.load(this.href, function() {
                    addDeleteConfirmEvent(commentBox);
                    addCommentLikeEvent(commentBox);
                });
                commentBox.toggle();
                return false;
            });
        });
    });
});
