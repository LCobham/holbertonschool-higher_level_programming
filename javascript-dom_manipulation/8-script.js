const apiURL = 'https://stefanbohacek.com/hellosalut/?lang=fr';
const element = document.querySelector('#hello');

fetch(apiURL, { mode: 'cors' })
  .then(response => response.json())
  .then(data => {
    element.textContent = data.hello;
  }).catch(err => console.log(err));
