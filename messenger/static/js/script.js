// Sticky Nav

$(function(){
  var header = $(".main-header");
  var triggerHeight = 0;
  $(window).scroll(function(){
    var scrollHeight = $(this).scrollTop();
    if(scrollHeight > triggerHeight){
      $(header).addClass("sticky");
    }
    else{
      $(header).removeClass("sticky");
    }
  });
});


// Fixed Inner Page Nav
$(function(){
  var innerHeader = $(".inner-page .main-header");
  $(innerHeader).addClass("sticky");
  $(window).scroll(function(){
      $(innerHeader).addClass("sticky");
  });
});


// Apartment Slider
$(document).ready(function(){
   $('.apartment-slider .slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    fade: true,
    asNavFor: '.slider-nav'
  });
  $('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.apartment-slider .slider',
    focusOnSelect: true,
    arrows: false
  });
});  


$(function(){
  var favTrigger = $('.add-to-fav');
  $(favTrigger).click(function(event){
    $(this).children().toggleClass("fa-heart-o fa-heart");
    event.preventDefault();
  });
});

$(function(){
  var box = $("#info-dialog");
  var headerHeight = $(".main-header").height();
  var offsetTop = $(box).offset().top;
  var offset = offsetTop - headerHeight;
  var sectionHeight = $(".apartment-slider").height() ;
  var netHeight = sectionHeight - $(box).height();
  console.log(offsetTop);
  $(window).scroll(function(){
    var scroll =$(this).scrollTop();
    // console.log(offset);
    if(scroll >= offset){
      $(box).addClass("fixed");
    }
    else{
      $(box).removeClass("fixed");
    }
    if (scroll >= netHeight){
      $(box).addClass("absolute");
    }
    else{
      $(box).removeClass("absolute");
    }
  });
});