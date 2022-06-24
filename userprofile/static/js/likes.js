$(function () {
  $(".profile .panel-body").click(function () {
    var profile_id = $(this).closest(".profile").attr("profile-id");
    location.href = "/userprofile/" + profile_id;
  });

  

  $(".profile").click(function () {
    var span = $(this);
    var profile = $(this).closest(".profile").attr("profile-id");
    var csrf = $("input[name='csrfmiddlewaretoken']", $(this).closest(".profile")).val();

    $.ajax({
      url: '/userprofile/like/',
      data: {
        'profile': profile,
        'csrfmiddlewaretoken': csrf
      },
      type: 'post',
      cache: false,
      success: function (data) {
        if ($(span).hasClass("liked")) {
          $(span).removeClass("glyphicon-heart")
            .removeClass("liked")
            .addClass("glyphicon-heart-empty");
        }
        else {
          $(span).removeClass("glyphicon-heart-empty")
            .addClass("glyphicon-heart")
            .addClass("liked");
        }
        $(".like-count").text(data);
      }
    });

  });
});