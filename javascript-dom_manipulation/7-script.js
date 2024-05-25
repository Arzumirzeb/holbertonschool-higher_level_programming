document.addEventListener('DOMContentLoaded', function() {
  const listMovies = document.getElementById('list_movies');
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => console.error('Error:', error));
});

