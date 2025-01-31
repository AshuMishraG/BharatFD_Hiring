A simple Django REST framework (DRF) API for managing FAQs with multilingual support.

🚀 Features

✅ CRUD operations for FAQs
✅ Multilingual support for English (en), Hindi (hi), and Bengali (bn)
✅ CKEditor for rich-text FAQ answers
✅ Redis-based caching for performance optimization

📦 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/AshuMishraG/BharatFD_Hiring

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

1️⃣ Get All FAQs

GET /api/faqs/

Response:

[
    {
        "id": 1,
        "translated_question": "What is Django?",
        "translated_answer": "A Python web framework."
    }
]

2️⃣ Get FAQs in Hindi

GET /api/faqs/?lang=hi

3️⃣ Create a New FAQ

POST /api/faqs/
Content-Type: application/json
{
    "question": "What is Django?",
    "answer": "A Python web framework.",
    "question_hi": "Django क्या है?",
    "answer_hi": "एक पायथन वेब फ्रेमवर्क।"
}

4️⃣ Update an FAQ

PUT /api/faqs/1/
Content-Type: application/json
{
    "question": "Updated Question?",
    "answer": "Updated Answer."
}

5️⃣ Delete an FAQ

DELETE /api/faqs/1/

⚡ Deployment

To deploy using Docker, create a Dockerfile:

FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "faq_project.wsgi:application"]

Then build & run:

docker build -t faq_api .
docker run -p 8000:8000 faq_api

🛠 Troubleshooting

Redis not running?
Start Redis manually:

brew services start redis

Database issues?
Try resetting migrations:

rm -rf faq/migrations
python manage.py makemigrations
python manage.py migrate

👨‍💻 Author

👤 Aashutosh Mishra
📧 aashutoshm77@gmail.com