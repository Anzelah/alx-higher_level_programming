document.addEventListener("DOMContentLoaded", () => {
  let url = 'https://www.fourtonfish.com/hellosalut/hello/';
  let langCode = $('#language_code').val();

  $('#btn_translate').click(function () {
    $.get(url + { langCode }, function(data) {
      $('#hello').html(data['hello']);
    });    
  });
});
