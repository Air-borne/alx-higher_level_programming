#!/usr/bin/node
// Print out the starwars characters

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Function to fetch character data and print the name
    const fetchCharacterData = (url) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Status Code:', response.statusCode);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    };

    // Fetch and print character names
    characterUrls.forEach(fetchCharacterData);
  }
});

