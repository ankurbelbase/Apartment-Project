$(function () {
  function refresh_messages() {
    $.ajax({
      url: '/messages/refresh/',
      cache: false,
      success: function () {
        $(".hello").load(' .hello');
      },
      complete: function () {
        window.setTimeout(refresh_messages, 10000);
      }
    });
  };
  refresh_messages();
});