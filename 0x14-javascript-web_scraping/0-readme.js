#!/usr/bin/node
//this script is intended to read and print the content of any given file

const fs = require('fs');

const file = process.argv.slice(2)[0];


fs.readFile(file, 'utf8', (err, data) => {
	if (err) {
	   console.log('errorhandling:', err);
	return;
	}
	
	// File contents are available in the `data` variable
	console.log(data);
});
