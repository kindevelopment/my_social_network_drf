Alimov Said

My social network drf

Проект представляет собой социальную сеть для рзработчиков. Где имеются команды - в которых можно состоять, чат для общения, личный профиль пользователя, возмонжость добавляться в друзья с другими пользователями. Возможность ставить оценку и оставлять комментарии под постами. Возможность выкладывать посты в сообществах.
## Старт
```
git clone https://github.com/kindevelopment/my_social_network_drf.git
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
- base - Базовые классы для переопределния метода get_permissions и get_serializers
- comments - Внутри модель для наследования абстрактной модели комментариев
- message_app - Приложение для чата между пользователями
- profile_app - Приложение профиля пользователя
- soical_project - config проекта DRF
- team_app - Приложение для работы с командами (группами)

## Используемы инструменты
- python - 3.10
- Django Rest Framework
- Django ORM
- postgres
- docker compose

