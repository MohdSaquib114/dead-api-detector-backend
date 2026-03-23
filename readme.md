# 🚀 Dead API Detector (FastAPI + PostgreSQL)

A backend system to monitor APIs, store logs, and calculate API health — designed to simulate a real-world API monitoring service.

---

# 📌 Features

* ✅ Create and manage APIs
* 📊 Track API health based on logs
* 📝 Store API response logs
* ⚡ Built with FastAPI + SQLAlchemy + Alembic

---

# 🏗️ Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Migrations:** Alembic
* **Server:** Uvicorn

---

# 📁 Project Structure

```
dead-api-detector/
│
├── alembic/              # Migration files
├── app/
│   ├── db/               # DB config & session
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API routes
│   ├── schema/           # Pydantic schemas
│   ├── services/         # Business logic
│   └── main.py           # Entry point
│
├── .env                  # Environment variables
├── alembic.ini
└── requirements.txt
```

---

# ⚙️ Setup & Run Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/MohdSaquib114/dead-api-detector-backend.git
cd dead-api-detector
```

---

## 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Mac/Linux
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup (PostgreSQL)

Make sure PostgreSQL is running.

Create database:

```sql
CREATE DATABASE dead_api;
```

---

# 🔐 Configure Environment Variables (IMPORTANT)

Create a `.env` file in the root directory:

```env
DB_USER=db_user
DB_PASSWORD=password
DB_HOST=db_host
DB_PORT=5432
DB_NAME=dead_api
```

---

# 🧬 Run Database Migrations

⚠️ Make sure `.env` is created BEFORE running migrations.

## 🔹 First Time Migration

```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

---

---

# 🚀 Run the Server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📘 Open Swagger UI (API Testing)

Open in browser:

```
http://127.0.0.1:8000/docs
```

👉 This is your frontend testing UI where you can:

* Create APIs
* Fetch APIs
* Check health
* View logs
* Delete APIs

---

# 🔍 Example API Usage

## ➤ Create API

```http
POST /apis
```

```json
{
  "name": "GitHub API",
  "url": "https://api.github.com",
  "method": "GET"
}
```

---

## ➤ Get All APIs

```http
GET /apis
```

---

## ➤ Check API Health

```http
GET /apis/{api_id}/health
```

---

## ➤ Get API Logs

```http
GET /apis/{api_id}/logs
```

---

## ➤ Delete API

```http
DELETE /apis/{api_id}
```

---

# 🧠 Notes

* `method` defaults to **GET**
* `created_at` is auto-generated
* Health depends on stored logs
* Ensure PostgreSQL is running before starting server

---


# 👨‍💻 Author

**Mohd Saquib Mansoori**

---

# ⭐ Summary

This project demonstrates:

* Clean backend architecture
* Database migrations using Alembic
* Real-world API monitoring logic

It serves as a strong backend project for showcasing **production-level concepts**.

---
