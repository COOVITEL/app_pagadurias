document.addEventListener("click", (e) => {
  const target = e.target;

  // Verifica que sea un botón que deba abrir el PDF
  if (target.matches(".btn-ver-pdf")) {
    const fileUrl = target.dataset.file;
    const iframe = document.getElementById("document");
    const dialog = document.getElementById("dialog");

    if (fileUrl && iframe && dialog) {
      iframe.src = fileUrl;
      dialog.showModal();
    }
  }

  // Botón de cerrar
  if (target.matches("#closeDialogBtn")) {
    const iframe = document.getElementById("document");
    const dialog = document.getElementById("dialog");

    if (iframe && dialog) {
      dialog.close();
      iframe.src = ""; // Limpia el iframe
    }
  }
});