require(['jquery'], function($) {
    $(function(){
        $('#mini-form-cmt-delete').submit(function(){
            return confirm("정말 삭제하시겠습니까?");
        });
    });
    $(function(){
        $('#mini-comment').click(function(){
            var post_id = document.getElementById("post-id").value;
            var elt = $('#comment-box-'+post_id);

            elt.load(this.href);
            elt.toggle();
            return false;
        });
    });
});
