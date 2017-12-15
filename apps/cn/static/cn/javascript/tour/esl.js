(function() {
  $(document).ready(function() {
    $('.weekend_event').hover(function(){
      $(this).css('background-color','black').css('color','white');
    },function(){
      $(this).css('background-color','white').css('color','black')
    })
    $('li').hover(function(){
      $(this).css('background-color','black').css('color','white');
    },function(){
      $(this).css('background-color','white').css('color','black')
    })
  });

}).call(this);
