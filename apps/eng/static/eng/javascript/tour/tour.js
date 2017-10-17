$(window).scroll(function() {
    if ($(".post1").position().top < $(document).scrollTop() + $(window).height()) {
        $(".post1").addClass("shift1")
    };
    if ($(".post2").position().top < $(document).scrollTop() + $(window).height()) {
        $(".post2").addClass("shift2")
    };
    if ($(".post3").position().top < $(document).scrollTop() + $(window).height()) {
        $(".post3").addClass("shift3")
    };
    if ($(".post4").position().top < $(document).scrollTop() + $(window).height()) {
        $(".post4").addClass("shift4")
    };
});
