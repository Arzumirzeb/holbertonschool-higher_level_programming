document.addEventListener('DOMContentLoaded', function() {
  const helloDiv = document.getElementById('hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));
});

