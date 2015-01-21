$(function() {
   $('#js-user-delete-form').submit(function () {
       return confirm('정말로?');
   });
});

var Profile = function(){
    var ns = {};

    ns.view = function() {

    };

    return ns;
}();
