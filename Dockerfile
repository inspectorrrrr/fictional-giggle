# Используем официальный образ Playwright для Python
FROM mcr.microsoft.com/playwright:v1.56.1-noble

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Создаем директории для результатов тестов
RUN mkdir -p allure-results allure-report

# Устанавливаем переменные окружения
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Команда по умолчанию для запуска тестов
CMD ["pytest", "tests/", "-v", "--alluredir=allure-results", "--browser=chromium"]

