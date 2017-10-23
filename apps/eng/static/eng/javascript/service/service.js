// $(document).ready(function(){
//   $( '.sidebar' ).fixedsticky();
//   // $('.scrollspy').scrollSpy();
// });

// var $window = window;
// var sidebar = document.querySelector('#sidebar');
//
// var offset = 50;
//
// window.addEventListener('scroll', function() {
//     // console.log('scroll');
//     if(window.scrollY >= offset) {
//         sidebar.style.marginTop = window.scrollY-offset+10 + 'px';
//     } else {
//         sidebar.style.marginTop = '0px';
//     }
// });

var asidePos = $('aside').offset().top;
var asideHeight = $('aside').outerHeight(true);


$(window).scroll(function(){
  if( $(this).scrollTop() > asidePos ) {
    $('body').addClass('sticky-aside');
  }
  else{
    $('body').removeClass('sticky-aside');
  }
});

//var footerPos = $('footer').offset().top;
var footerPos = $('footer').offset().top;
var docHeight = $(document).height();
$(window).scroll(function(){
var scrollPos = $(this).scrollTop() + $('aside').height();
  if( scrollPos > footerPos ) {
    $('body').addClass('remove-sticky-aside');
    //alert('1')
  }
  else{
    $('body').removeClass('remove-sticky-aside');
  }
});
