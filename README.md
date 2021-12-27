# watching-storage-django-orm

Сайт который можно подключить к удаленной Базе Данных (далее БД)  
Отображает:  
* Активные карты доступа сотрудников
* Выводит информацию по каждому сотруднику о визитах в определенную зону (*в данном случае визиты в хранилище)  
* Показывает в рельном времени кто из сотрудников находится в хранилище

### Как установить


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Запуск осуществляется на localhost:8080 с помощью команды:  
```
python manage.py runserver 0.0.0.0:8000
```

project/settings.py - настройка подключения к БД, необходимо:  
1.    создать файл .env с перемеными окружения (подробнее https://pypi.org/project/python-dotenv/)
2.    обозначить в файле следующие переменные:  
```
  DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME_BD
  SECRET_KEY = <...>
  ALLOWED_HOSTS = '127.0.0.1'
  DEBUG = <true/false>
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
