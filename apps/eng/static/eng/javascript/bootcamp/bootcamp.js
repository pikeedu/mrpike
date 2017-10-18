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

                $(this).animate({'opacity':'1'},2000);

            }

        });

    });

    // Hexagon Image
    var color = 'one';
    var counter = 0;
    $('.desc').hide();
    $('.hexagon').hover(
      function() {
        $(this).find('.desc').fadeIn('fast');
        counter++;
        if (counter === 0) {
          color = 'base';
        } else if (counter === 1) {
          color = 'one';
        } else if (counter === 2) {
          color = 'two';
        } else if (counter === 3) {
          color = 'three';
        } else if (counter >= 4){
          counter = 0 ;
          color = 'base';
        }
        $(this).find('.desc').addClass(color);
      },
      function() {
        $(this).find('.desc').fadeOut('fast', function() {
          $(this).removeClass(color);
        });
      });


});
