#!/usr/bin/node

let filePath = process.argv[2];
const fs = require('fs');

fs.readFile('filePath', 'utf8', function (err, data) => {
	if (err) {
		console.error(err);
	}
	console.log(data);
});
