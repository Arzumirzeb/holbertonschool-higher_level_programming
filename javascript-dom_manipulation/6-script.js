document.addEventListener('DOMContentLoaded', function() {
  const characterDiv = document.getElementById('character');
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      characterDiv.textContent = data.name;
    })
    .catch(error => console.error('Error:', error));
});

