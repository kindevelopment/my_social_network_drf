Omelchenko Michael
junov_net

Edit README and fix db
SouLWorkeR authored 1 month ago
a3f1678f
junov_net
README.md
README.md
4.97 KiB
# JunovNet
Проект представляет собой веб-приложение для ментора и менти, которое позволяет управлять списком 
студентов, расписанием занятий, домашними заданиями и дополнительными материалами. Приложение также 
интегрируется с Google Календарем для удобства управления расписанием.
## Старт
```
git clone https://gitlab.com/DJWOMS/junov_net.git
Переименовать .env.example на .env
docker-compose up --build
```
## Создание миграций
1) В `migrations/base.py` импортировать модуль с моделями.
2) Выполнить команду создания файла миграций.
```
alembic revision --autogenerate -m 'название модели или миграции'
```
3) Проверить созданный файл миграций. Alembic не умеет работать с переименованием таблиц и полей.
4) Выполнить миграцию (изменения в бд)
```
alembic upgrade head
```
## Запуск проекта
1) Запускаем проект коммандой:
```
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000 --log-level debug --use-colors
```
2) Переходим по ссылке: http://127.0.0.1:8000/docs
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
## Files
Каждый пакет (приложение) имеет свои router, schemas, models и т.д.
- repository.py - repository
- controllers.py - ядро каждого модуля со всеми endpoints
- service.py - специфичная для модуля бизнес-логика
- models.py - для моделей БД
- schemas.py - для pydantic моделей
- routers.py - общие routers для всех контроллеров модуля
- dependencies.py - зависимости для приложения
- utils.py - функции, не относящиеся к бизнес-логике
- exceptions.py - специфические для модуля исключения
- constants.py - константы
## Используемы инструменты
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106

- python - 3.11
- fastapi - 0.100.0
- sqlalchemy - 2.0.18
- postgres - 15.3
- docker compose - 3.9

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/DJWOMS/junov_net/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***



## License
For open source projects, say how it is licensed.
