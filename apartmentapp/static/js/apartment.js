$(function () {
  $(".apartment .panel-body").click(function () {
    var profile_id = $(this).closest(".apartment").attr("apartment_id");
    location.href = "/apartment/apartment-detail/" + apartment_id;
  });

  

  $(".favorite").click(function () {
    var span = $(this);
    var apartment = $(this).closest(".apartment").attr("apartment-id");
    var csrf = $("input[name='csrfmiddlewaretoken']", $(this).closest(".apartment")).val();

    $.ajax({
      url: '/apartment/apartment-detail/like/',
      data: {
        'apartment': apartment,
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