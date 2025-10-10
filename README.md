# doozy

__doozy__ - простое и стильное веб-приложение для управления задачами.

<a name="Начало"></a>

- [Описание](#Описание "Перейти")
- [Технологии](#Технологии "Перейти")
- [Шаблон заполнения .env-файла](#Шаблон "Перейти")
- [Запуск проекта на локальной машине](#Запуск "Перейти")
- [Автор](#Автор "Перейти")


<a name="Описание"></a>

## Описание

__doozy__ — это веб-приложение для управления задачами (TODO), разработанное на Django с использованием Bootstrap 5.
Цель проекта — предоставить простой, минималистичный интерфейс, где пользователь может

- создавать задачи с заголовком и описанием
- задавать срок выполнения (дата и время)
- отмечать задачи как выполненные
- удалять задачи
- редактировать профиль, в том числе имя, фамилию, логин, email
- восстановление пароля по email с интеграцией SMTP
- кастомные страницы ошибок (404, 403, 500) в едином стиле

<a name="Технологии"></a>

## Технологии

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

[Вернуться в начало](#Начало "Перейти")

<a name="Шаблон"></a>

#### Шаблон заполнения .env-файла, расположен в корне проекта

##### С настройкой отправки e-mail можно ознакомиться в документации [Яндекс](https://yandex.ru/support/mail/mail-clients/others.html "Перейти") или в документации любой другой почты

###### (в settings.py указаны дефолтные значения для переменных из env-файла)

```python
SECRET_KEY = 'Ваш секретный ключ'

EMAIL_BACKEND = 'Почтовый SMTP-бэкенд'
EMAIL_HOST = 'Адрес почтового сервера'
EMAIL_PORT = Порт
EMAIL_USE_SSL = Защита соединения
EMAIL_HOST_USER = 'E-mail адрес'
EMAIL_HOST_PASSWORD = 'Сгенерированный пароль для приложения' 
```

[Вернуться в начало](#Начало "Перейти")

<a name="Запуск"></a>

## Запуск проекта на локальной машине

- __Склонируйте репозиторий__

```python
git clone git@github.com:dmsnback/doozy.git
```

- __Установите и активируйте виртуальное окружение__

```python
python3 -m venv venv
```

Для ```Windows```

```python
source venv/Scripts/activate
```

Для ```Mac/Linux```

```python
source venv/bin/activate
```

- __Установите зависимости из файла__ ```requirements.txt```

```python
python3 -m pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

- __В корневой директории создайте файл__ ```.env```

### ([Шаблон заполнения .env-файла](#Шаблон "Перейти"))

#### (С настройкой отправки e-mail можно ознакомиться в документации [Яндекс](https://yandex.ru/support/mail/mail-clients/others.html "Перейти") или в документации любой другой почты.)

```python
SECRET_KEY = 'Ваш секретный ключ'

EMAIL_BACKEND = 'Почтовый SMTP-бэкенд'
EMAIL_HOST = 'Адрес почтового сервера'
EMAIL_PORT = Порт
EMAIL_USE_SSL = Защита соединения
EMAIL_HOST_USER = 'E-mail адрес'
EMAIL_HOST_PASSWORD = 'Сгенерированный пароль для приложения' 
```

- __Перейдите в директорию с проектом__ 

```python
cd doozy
```

- __Выполните миграции__

Для ```Windows```

```python
python manage.py migrate
```

Для ```Mac/Linux```

```python
python3 manage.py migrate
```

- __Запустите приложение__

Для ```Windows```

```python
python manage.py runserver
```

Для ```Mac/Linux``

```python
python3 manage.py runserver
```

- __Проект доступен по ссылке__

 [http://127.0.0.1:8000/](http://127.0.0.1:8000/ "Перейти")

## License

[MIT](https://choosealicense.com/licenses/mit/)

<a name="Автор"></a>

## Автор

- [Титенков Дмитрий](https://github.com/dmsnback "Перейти")

[Вернуться в начало](#Начало "Перейти")
