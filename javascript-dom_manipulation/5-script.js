document.addEventListener('DOMContentLoaded', function() {
  const updateHeaderButton = document.getElementById('update_header');
  const header = document.querySelector('header');

  updateHeaderButton.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
  });
});

