Alimov Said
My social network drf

Проект представляет собой социальную сеть для рзработчиков. Где имеются команды - в которых можно состоять, чат для общения, личный профиль пользователя, возмонжость добавляться в друзья с другими пользователями. Возможность ставить оценку и оставлять комментарии под постами. Возможность выкладывать посты в сообществах.
## Старт
```
git clone https://gitlab.com/DJWOMS/junov_net.git
Переименовать .env.example на .env
docker-compose up --build
```
## Создание миграций
1) Для создания миграций, нужно будет выполнить команду.
```
Python3 manage.py makemigrations
```
2) Для применения миграций применить команду.
```
Python3 manage.py makemigrations
```
## Запуск проекта
1) Запускаем проект коммандой:
```
Python3 manage.py runserver
```
2) Переходим по ссылке: http://127.0.0.1:8000
## Folders
- core - директория для общих настроек
- core/db.py - настройки базы данных
- core/settings.py - настройки для проекта
- core/db/session.py - настройки сессии БД
- core/share - базовые классы для controllers, models, services и т.д.
- media - media файлы: картинки, pdf и т.д.
- static - static файлы: css, js и т.д.
- migrations - директория alembic для миграций
- migrations/versions - файлы миграций
- migrations/base.py - файл с импортированными модулями моделей для работы автогенерации миграций
- migrations/env.py - скрипт alembic для работы миграций
- src - верхний уровень приложения, содержит общие маршруты, main.py, все сервисы (приложения)
- src/main.py - корень проекта, который запускает приложение FastAPI
- src/routers.py - общие routers для всех приложений проекта

## Используемы инструменты
- python - 3.10
- Django Rest Framework
- Django ORM
- postgres
- docker compose

