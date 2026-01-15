# 🚗 Used Car Price Prediction

End-to-end machine learning project for predicting used car prices.

## Tech Stack
- Python
- Scikit-learn
- FastAPI (Backend API)
- Streamlit (Frontend UI)

## Features
- Feature engineering
- ML pipeline
- REST API
- Interactive web app

## How to Run Locally

### Backend
```bash
uvicorn api.app:app --reload

### Frontend
python -m streamlit run frontend/app.py


Save file.

---

## 🧩 PART B — INITIALIZE GIT (VS CODE TERMINAL)

### ✅ B1. Open VS Code terminal

Top menu → **Terminal → New Terminal**

Make sure you are in:


Verify:
```bash
pwd        # Mac/Linux
cd         # Windows





## How to Run the Project

### 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 2. Install dependencies
pip install -r requirements.txt

### 3. Start backend (Terminal 1)
uvicorn api.app:app --reload

### 4. Start frontend (Terminal 2)
streamlit run frontend/app.py

### 5. Open browser
Backend: http://127.0.0.1:8000/docs  
Frontend: http://localhost:8501

