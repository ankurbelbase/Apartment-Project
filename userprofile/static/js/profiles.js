$(function () {
  $(".question .panel-body").click(function () {
    var profile_id = $(this).closest(".question").attr("profile-id");
    location.href = "/userprofile/" + profile_id;
  });

  

  $(".favorite").click(function () {
    var span = $(this);
    var profile = $(this).closest(".question").attr("profile-id");
    var csrf = $("input[name='csrfmiddlewaretoken']", $(this).closest(".question")).val();

    $.ajax({
      url: '/userprofile/favorite/',
      data: {
        'profile': profile,
        'csrfmiddlewaretoken': csrf
      },
      type: 'post',
      cache: false,
      success: function (data) {
        if ($(span).hasClass("favorited")) {
          $(span).removeClass("glyphicon-star")
            .removeClass("favorited")
            .addClass("glyphicon-star-empty");
        }
        else {
          $(span).removeClass("glyphicon-star-empty")
            .addClass("glyphicon-star")
            .addClass("favorited");
        }
        $(".favorite-count").text(data);
      }
    });

  });
});