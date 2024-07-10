#!/usr/bin/node

const request = require("request");
// get the film exact no from the arguments
const ttlfilmNo = process.argv[2] + "/";
// get base URL from the endpnt
const filmapiURL = "https://swapi-api.hbtn.io/api/films/";

// API req
request(filmapiURL + ttlfilmNo, async function (err, res, body) {
	if (err) return console.error(err);
	// Parse the response body to get the list of chars URLs
	const charURLSt = JSON.parse(body).characters;
	// Iterate thru the list of char URLs to fetch nd print each char's name
	for (const charactrURL of charURLSt) {
		// Use a promise to handle the asynchronous request
		await new Promise(function (resolve, reject) {
			request(charactrURL, function (err, res, body) {
				if (err) return console.error(err);
			// Parse the char's info
				console.log(JSON.parse(body).name);
				// Resolve the promise to indicate that
				// the request for this character's information is complete
				resolve();
			});
		});
	}
});
