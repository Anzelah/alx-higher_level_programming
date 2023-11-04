document.addEventListener("DOMContentLoaded", () => {
  $(function() {
    let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function(data, textStatus) {
      let res = data['hello'];
      $('#hello').text(res);
    });
  });
});;
