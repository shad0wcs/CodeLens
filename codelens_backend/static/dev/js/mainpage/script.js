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

function copyToClipboard() {
    const resultBox = document.getElementById("resultBox"); // Ссылка на блок с кодом
    const textToCopy = resultBox.innerText || resultBox.textContent; // Получаем содержимое блока

    navigator.clipboard.writeText(textToCopy) // Копируем текст в буфер
        .then(() => {
            // Временное уведомление о копировании
            const originalContent = resultBox.innerHTML;
            resultBox.innerHTML = "<p>Скопировано в буфер обмена!</p>"; // Уведомление
            setTimeout(() => {
                resultBox.innerHTML = originalContent; // Возвращаем оригинальный текст через 1.5 сек
            }, 1000);
        })
        .catch(err => {
            console.error("Ошибка копирования: ", err);
            alert("Не удалось скопировать. Попробуйте снова.");
        });
}