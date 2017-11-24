(function() {
  $(document).ready(function() {
    $('.list-group-item').hover(function(){
      $(this).css('background-color','black').css('color','white');
    },function(){
      $(this).css('background-color','white').css('color','black')
    })
  });

}).call(this);
