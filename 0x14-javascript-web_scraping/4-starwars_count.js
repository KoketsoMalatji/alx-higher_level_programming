#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let count = 0;
    let findCharacter = [];
    const filmsResults = JSON.parse(body).results;
    for (const film of filmsResults) {
      findCharacter = film.characters.filter(value => value.indexOf('18/') !== -1);
      if (findCharacter) {
        count += findCharacter.length;
      }
    }
    console.log(count);
  }
});
