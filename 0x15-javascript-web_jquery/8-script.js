$(function() {
  let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function(data, textStatus) {
    res = data['results'];
    $.each(res, function(i, results) {
      let movies = results['title'];
      $('#list_movies').append('<li>' + movies + '</li>');
    });     
  });     
});
