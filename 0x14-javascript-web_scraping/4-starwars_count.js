#!/usr/bin/node
//This script prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

function countMoviesWithCharacter(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status Code:', response.statusCode);
    } else {
      const filmData = JSON.parse(body);
      const moviesWithCharacter = filmData.results.filter(film =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log( moviesWithCharacter.length);
    }
  });
}

// Usage: Pass the Star Wars API URL as an argument
const apiUrl = process.argv[2];
countMoviesWithCharacter(apiUrl);

