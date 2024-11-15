// Функция переключения темы
function toggleTheme() {
    document.body.classList.toggle("dark-theme");
    document.body.classList.toggle("light-theme");
}

// Установка начальной темы
document.addEventListener("DOMContentLoaded", function() {
    const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (isDarkMode) {
        document.body.classList.add("dark-theme");
    } else {
        document.body.classList.add("light-theme");
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const uploadBox = document.getElementById("uploadBox");
    const fileInput = document.getElementById("fileInput");
    const fileNameDisplay = document.getElementById("fileName");

    // Обработчик клика для открытия окна выбора файла
    uploadBox.addEventListener("click", () => {
        fileInput.click();
    });

    // Обработчик для выбора файла через стандартный input
    fileInput.addEventListener("change", () => {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = `Вы выбрали: ${fileInput.files[0].name}`;
        }
    });

    // Обработчик для dragover (чтобы разрешить перетаскивание)
    uploadBox.addEventListener("dragover", (e) => {
        e.preventDefault();
        uploadBox.classList.add("drag-over"); // Добавляем класс для стиля
    });

    // Обработчик для dragleave (убираем стиль при покидании зоны)
    uploadBox.addEventListener("dragleave", () => {
        uploadBox.classList.remove("drag-over");
    });

    // Обработчик drop для получения файла
    uploadBox.addEventListener("drop", (e) => {
        e.preventDefault();
        uploadBox.classList.remove("drag-over"); // Убираем стиль

        // Получаем файл из события drop
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files; // Присваиваем файлы input'у
            fileNameDisplay.textContent = `Вы выбрали: ${files[0].name}`;
        }
    });
});