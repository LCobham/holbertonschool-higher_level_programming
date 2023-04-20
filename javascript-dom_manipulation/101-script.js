document.addEventListener('DOMContentLoaded', () => {
  const apiURL = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const languageCode = document.getElementById('language_code');
  const translateButton = document.getElementById('btn_translate');
  const helloTag = document.getElementById('hello');

  translateButton.addEventListener('click', () => {
    const selectedOption = languageCode.options[languageCode.selectedIndex].value;
    if (selectedOption) {
      fetch(apiURL + selectedOption)
        .then(response => response.json())
        .then(data => {
          helloTag.textContent = data.hello;
        })
        .catch(err => console.error(err));
    }
  });
});
