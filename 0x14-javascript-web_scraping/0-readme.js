#!/usr/bin/node
let filePath = process.argv[2];

const fs = require('fs');

fs.readFile('filePath', 'utf-8',  (err, data) => {
	if (err) {
		console.error('doesntexist');
		console.error(err);
		return;
	}
	console.log(data);
});
