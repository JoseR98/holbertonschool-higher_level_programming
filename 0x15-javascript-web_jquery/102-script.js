$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, (response) => {
      $('div#hello').text(response.hello);
    });
  });
});
