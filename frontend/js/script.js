// Получаем кнопку переключения темы
const themeToggle = document.getElementById('theme-toggle');

// Добавляем обработчик клика
themeToggle.addEventListener('click', () => {
    // Переключаем класс на body
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    // Меняем текст кнопки в зависимости от темы
    if (document.body.classList.contains('light-theme')) {
        themeToggle.textContent = 'Сменить на тёмную тему';
    } else {
        themeToggle.textContent = 'Сменить на светлую тему';
    }
});
