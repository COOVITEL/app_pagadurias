const toggle = document.getElementById('menu-toggle');
const menuSettings = document.getElementById('menu-settings');

toggle.addEventListener('click', () => {
    menuSettings.classList.toggle('hidden');
});
