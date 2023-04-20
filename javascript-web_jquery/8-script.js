$(() => {

  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    contentType: 'application/json',
    succes: data => {
      for (const film of data.results) {
        $('UL#list_movies').append(`<li>${film.title}<\li>`);
      }
    },
    error: err => { console.log(err) }
  })
});