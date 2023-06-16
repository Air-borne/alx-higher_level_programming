#!/usr/bin/node
//this script is intended to write a string and pto the content of any given file

const fs = require('fs');

const file = process.argv.slice(2)[0];

const newText = process.argv.slice(3)[0];

fs.appendFile(file, newText, 'utf8', (err, data) => {
	if (err) {
	   console.log('errorhandling:', err);
	}
	return;
});
