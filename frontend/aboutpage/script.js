// Установка начальной темы на основе локального хранилища или предпочтений пользователя
document.addEventListener("DOMContentLoaded", function() {
    const isDarkThemePreferred = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme) {
        document.body.classList.add(savedTheme);
    } else {
        document.body.classList.add(isDarkThemePreferred ? "dark-theme" : "light-theme");
    }
});

// Обновление toggleTheme для сохранения выбора пользователя
function toggleTheme() {
    if (document.body.classList.contains("dark-theme")) {
        document.body.classList.remove("dark-theme");
        document.body.classList.add("light-theme");
        localStorage.setItem("theme", "light-theme");
    } else {
        document.body.classList.remove("light-theme");
        document.body.classList.add("dark-theme");
        localStorage.setItem("theme", "dark-theme");
    }
}
