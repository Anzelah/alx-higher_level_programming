$(function () {
  let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data, textStatus) {
    let res = data['name'];
    $('#character').append(res);
  });
});
