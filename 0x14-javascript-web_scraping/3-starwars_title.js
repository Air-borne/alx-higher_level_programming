#!/usr/bin/node
//This script would return the title of the movie from starwars

const request = require('request');

function getMovieTitle(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status Code:', response.statusCode);
    } else {
      const movieData = JSON.parse(body);
      console.log( movieData.title);
    }
  });
}

// Usage: Pass the desired movie ID as an argument
const movieId = process.argv[2];
getMovieTitle(movieId);

