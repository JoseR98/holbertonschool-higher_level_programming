$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (json) => {
  $('div#character').text(json.name);
});
