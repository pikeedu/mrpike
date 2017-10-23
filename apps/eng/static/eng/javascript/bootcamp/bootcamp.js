$(function(){  // $(document).ready shorthand
  $('.monster').fadeIn('slow');
});

$(document).ready(function() {

    /* Every time the window is scrolled ... */
    $(window).scroll( function(){

        /* Check the location of each desired element */
        $('.hideme').each( function(i){

            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            /* If the object is completely visible in the window, fade it it */
            if( bottom_of_window > bottom_of_object ){

                $(this).animate({'opacity':'1'},1000);

            }

        });

    });

});

var fullPageModal = (function ($) {
    var fpm = {};

    fpm.config = {
        $target : $(".js__target"),
        $pages : $("a.page"),
        $close : $(".js__target .js__close")
    };
    fpm.init = function () {
        fpm.ui();
    };
    fpm.ui = function () {
        fpm.config.$pages.on("click", this, function(e) {
            e.preventDefault();
            fpm.loadPage($(this).attr("href"), $(this));

        });
        fpm.config.$close.on("click", this, function(e) {
            e.preventDefault();
            fpm.closePage();
        });
    };
    fpm.loadPage = function(pageToLoad, page) {
        var $content = fpm.config.$target.find(".content");
        $.ajax({
            async: false,
            url: pageToLoad,
            dataType: 'html',
            success: function(res) {
                $content.html($(res).find("#content"));
            }
        });
        fpm.openPage(page);
    };
    fpm.openPage = function (page) {
        var offset = $(page).offset();
        fpm.config.$target
            .css({"left" : offset.left, "top" : offset.top, "width" : $(page).outerWidth(), "height" : $(page).outerHeight()})
            .addClass("open");
      setTimeout(
              function() {
                  fpm.config.$target.addClass("expand").addClass("move");
              }, 500 //this should not be less than the ms value in .js__target.move
        );

    };
    fpm.closePage = function () {
        fpm.config.$target.removeClass("expand");
        setTimeout(
            function() {
                fpm.config.$target.removeClass("open");
            }, 500 //this should not be less than the ms value in .js__target.move
        );
    };
    return fpm;
})(jQuery);

$(function () {
    fullPageModal.init();
});
