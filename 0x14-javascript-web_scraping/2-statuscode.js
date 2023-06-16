#!/usr/bin/node
// This script outputs to the screen the status code

const request = require('request');

const url = process.argv.slice(2)[0];

request(url, (error, response) => {
	if(error){
	  console.log(error);
	  return;
	}
	const statusCode = response.statusCode;
	console.log('code:', statusCode);

});

