const messages = [
    "Validando ciudades y departamentos...",
    "Procesando información...",
    "Preparando todo...",
    "Casi listo..."
];

let intervalID = null;

function showLoadingOverlay() {
    const loadingOverlay = document.getElementById("loadingOverlay");
    const loadingText = document.getElementById("loadingText");

    if (!loadingOverlay || !loadingText) return;

    loadingOverlay.style.display = "flex";

    if (!loadingOverlay.classList.contains("messages-active")) {
        loadingOverlay.classList.add("messages-active");

        let index = 0;
        loadingText.style.opacity = 0;
        loadingText.textContent = messages[index];
        loadingText.style.opacity = 1;
        index = (index + 1) % messages.length;
    }
}

function hideLoadingOverlay() {
    const loadingOverlay = document.getElementById("loadingOverlay");
    if (loadingOverlay) {
        loadingOverlay.style.display = "none";
        loadingOverlay.classList.remove("messages-active");
    }
    if (intervalID) {
        intervalID = null;
    }
}