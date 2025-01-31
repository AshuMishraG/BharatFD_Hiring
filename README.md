# 📝 FAQ Management API (Django REST Framework)

A simple Django REST framework (DRF) API for managing FAQs with multilingual support.

---

## 📷 Screenshots

1. **FAQ List View**  
   ![http://127.0.0.1:8000/](./screenshot1.png)

2. **Create FAQ Form**  
   ![http://127.0.0.1:8000/api/faqs/?lang=hi](./screenshot2.png)

3. **FAQ Detail View**  
   ![http://127.0.0.1:8000/api/faqs/](./screenshot3.png)

---

## 🚀 Features

✅ CRUD operations for FAQs  
✅ Multilingual support: **English (en), Hindi (hi), Bengali (bn)**  
✅ CKEditor for rich-text FAQ answers  
✅ Redis-based caching for performance optimization  

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AshuMishraG/BharatFD_Hiring
cd BharatFD_Hiring

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Run Development Server

python manage.py runserver

API is now accessible at: http://127.0.0.1:8000/api/faqs/

📡 API Endpoints

➤ Get All FAQs

GET /api/faqs/

➤ Get FAQs in Hindi

GET /api/faqs/?lang=hi

➤ Create a New FAQ

POST /api/faqs/
{
    "question": "What is Django?",
    "answer": "A Python web framework.",
    "question_hi": "Django क्या है?",
    "answer_hi": "एक पायथन वेब फ्रेमवर्क।"
}

➤ Update an FAQ

PUT /api/faqs/1/
{
    "question": "Updated Question?",
    "answer": "Updated Answer."
}

➤ Delete an FAQ

DELETE /api/faqs/1/

⚡ Deployment

For Docker Deployment:

docker build -t faq_api .
docker run -p 8000:8000 faq_api

🛠 Troubleshooting
	•	Redis not running? Start it with:

brew services start redis

	•	Database issues? Reset migrations:

rm -rf faq/migrations
python manage.py makemigrations
python manage.py migrate

👤 Author: Aashutosh Mishra
📧 Email: aashutoshm77@gmail.com