document.getElementById('update-pagaduria').addEventListener('submit', () => {
  const btn = document.getElementById('update-btn');
  btn.disabled = true; // Desactiva el botón
  btn.classList.add('cursor-not-allowed', 'opacity-50'); // Opcional: hace que se vea desactivado

  // Opcional: cambia el texto mientras se procesa
  btn.innerText = 'Enviando...'; 
});