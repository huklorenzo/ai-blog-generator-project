# 📘 AI-Powered Blog Generator

A full-stack web application that generates blog posts powered by AI.  
Built with **FastAPI** (Python) on the backend and **React** (JavaScript) on the frontend.  
Integrates with **OpenAI's GPT models** to produce unique articles from user-submitted topics.

---

## ✨ Features

- ✍️ Generate AI-written blog articles from a given topic
- 📚 View, edit, and delete saved blog posts
- ⚡ FastAPI backend with async API handling
- ⚛️ Clean and responsive React frontend
- 💾 Database storage (PostgreSQL or SQLite)
- 🔐 Secure environment variables (.env for API keys and DB URL)
- 🚀 Deployed backend (Render) and frontend (Vercel)

---

## 🛠️ Tech Stack

- **Frontend**: React, Axios
- **Backend**: FastAPI, OpenAI Python SDK
- **Database**: PostgreSQL (Production), SQLite (Local Dev)

---

## Setup

### Backend
1. Download requirements
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a .env file inside backend/:
```
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=sqlite:///./blog.db
```

3. Run the Postgres DB and FastAPI server:
```bash
brew services start postgresql
uvicorn app.main:app --reload
```

### Frontend
Install and run:
```bash
npm install
npm start
```
