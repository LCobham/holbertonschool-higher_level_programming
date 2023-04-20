const requestURL = 'https://swapi-api.hbtn.io/api/films/?format=json';
const ulElement = document.querySelector('ul#list_movies');

fetch(requestURL)
  .then(
    response => response.json()
  )
  .then(data => {
    for (const movie of data.results) {
      const liElement = document.createElement('li');
      liElement.textContent = movie.title;
      ulElement.append(liElement);
    }
  })
  .catch(err => console.log(err));
