$(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: data => {
      $('DIV#hello').text(data.hello);
    },
    error: err => console.log(err)
  });
});
