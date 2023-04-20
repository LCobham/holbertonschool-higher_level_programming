document.addEventListener('DOMContentLoaded', () => {
  const apiURL = ' https://hellosalut.stefanbohacek.dev/?lang=fr';
  const element = document.querySelector('#hello');

  fetch(apiURL)
    .then(response => response.json())
    .then(data => {
      element.textContent = data.hello;
    }).catch(err => console.log(err));
});
