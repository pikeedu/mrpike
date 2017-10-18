$(document).ready(function(){
  $('.scrollspy').scrollSpy();
});

// var $window = window;
var sidebar = document.querySelector('#sidebar');

var offset = 50;

window.addEventListener('scroll', function() {
    // console.log('scroll');
    if(window.scrollY >= offset) {
        sidebar.style.marginTop = window.scrollY-offset+10 + 'px';
    } else {
        sidebar.style.marginTop = '0px';
    }
});
