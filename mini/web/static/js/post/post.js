require(['jquery'], function ($) {
    $(function () {
        $('.mini-form-post-delete').submit(function () {
            return confirm("정말 삭제하시겠습니까?");
        });
    });
    $(function () {
        $('.mini-post').each(function() {
            var likes = $(this).find('.post-like-count');
            $(this).find('.post-like').click(function () {
                $.post(this.href,
                    function (response, status) {
                        var json_response = $.parseJSON(response);
                        if(json_response.like_count != '0')
                        likes.text(json_response.like_count);
                        else
                        likes.text('');
                    });
                return false;
            });
        });
    });
});