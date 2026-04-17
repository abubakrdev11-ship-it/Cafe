# ☕ Cafe API

## 📌 Описание

Проект представляет собой API для кофейни, где пользователи могут создавать и управлять заказами.

---

## 🚀 Функционал

* Создание заказа
* Просмотр всех заказов
* Принятие заказа
* Закрытие заказа

---

## 🔐 Валидация

* Изменять заказ может только пользователь, который его создал
* Просматривать заказы могут все авторизованные пользователи

---

## 🛠 Технологии

* Python
* Django
* Django REST Framework

---

## 📂 Структура проекта

* users — приложение для пользователей
* orders — приложение для заказов

---

## ⚙️ Установка

```bash
git clone <your-repo-link>
cd Cafe
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Запуск проекта

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔑 Создание суперпользователя

```bash
python manage.py createsuperuser
```

---

## 📡 API эндпоинты

* `POST /api/orders/create/` — создать заказ
* `GET /api/orders/` — список заказов
* `POST /api/orders/accept/` — принять заказ
* `POST /api/orders/close/` — закрыть заказ

---

## 📘 Swagger документация

```id="doclink"
http://127.0.0.1:8000/swagger/
```

---

## 📌 Автор

Abubakr
