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

// Копирование кода
function copyToClipboard() {
    const resultBox = document.getElementById("resultBox"); // Ссылка на блок с кодом
    const textToCopy = resultBox.innerText || resultBox.textContent; // Получаем содержимое блока

    navigator.clipboard.writeText(textToCopy) // Копируем текст в буфер
        .then(() => {
            // Временное уведомление о копировании
            const originalContent = resultBox.innerHTML;
            resultBox.innerHTML = "<p>Скопировано в буфер обмена!</p>"; // Уведомление
            setTimeout(() => {
                resultBox.innerHTML = originalContent;
            }, 1000);
        })
        .catch(err => {
            console.error("Ошибка копирования: ", err);
            alert("Не удалось скопировать. Попробуйте снова.");
        });
}

// Имя файла
const fileInput = document.querySelector("input[type='file']");
const fileNameDisplay = document.getElementById("fileNameDisplay");

if (fileInput) {
    fileInput.addEventListener("change", function () {
        if (this.files && this.files[0]) {
            fileNameDisplay.textContent = this.files[0].name;
        } else {
            fileNameDisplay.textContent = "Файл не выбран";
        }
    });
}
