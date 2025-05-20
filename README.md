# Flask Request Viewer

## Описание

Веб-приложение на Flask для отображения данных запроса, авторизации и проверки номера телефона.

## Запуск

```bash
pip install flask
python app.py
```

## Страницы

- `/request-info`: отображает параметры URL, заголовки, cookies.
- `/login`: форма авторизации с выводом введенных данных.
- `/phone`: форма проверки номера телефона с валидацией и форматированием.

## Деплой

Можно развернуть на Render, Railway, Heroku или любом WSGI-хостинге.

## Пример URL

```
/request-info?param1=one&param2=two&param3=three&param4=four
```

## Автор

Разработано как часть учебного задания по Flask.
