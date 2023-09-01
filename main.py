# Practice API Call
# https://rapidapi.com/soyamchinglemba/api/imdb_api4/

const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://imdb_api4.p.rapidapi.com/get_movies_by_cast_name',
  headers: {
    'X-RapidAPI-Key': '6d84a55e3bmsh487c9b6e29c1760p1d0072jsn49a780a77f59',
    'X-RapidAPI-Host': 'imdb_api4.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}