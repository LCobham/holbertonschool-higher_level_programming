const starWarsCharacter = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => starWarsCharacter.textContent = data.name)
  .catch(err => console.error(err));
