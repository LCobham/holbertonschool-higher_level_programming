$(() => {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    type: 'GET',
    contentType: 'application/json',
    success: data => {
      for (const film of data.results) {
        $('UL#list_movies').append(`<li>${film.title}</li>`);
      }
    },
    error: err => { console.log(err); }
  });
});
