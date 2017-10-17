$(document).ready(function(){
  $('.carousel').carousel({
    interval: 2000
  });
  $('.dropdown-toggle').dropdown();

})

$(window).scroll(function() {
  if ($(".post-left").position().top < $(document).scrollTop() + $(window).height()) {
    $(".post-left").addClass("shift-left")
  };
  if ($(".post-right").position().top < $(document).scrollTop() + $(window).height()) {
    $(".post-right").addClass("shift-right")
  };

})
