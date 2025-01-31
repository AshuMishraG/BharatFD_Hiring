# Django FAQ API with Multilingual Support

    ## Project Description

    This project implements a Django REST API for managing Frequently Asked Questions (FAQs) with multilingual support. It includes a WYSIWYG editor for rich text answers and caching for optimized performance.

    ## Installation

    1. Clone the repository.
    2. Navigate to the project directory: `cd faq_project`
    3. Install dependencies: `pip install -r requirements.txt`
    4. Set up the database and run migrations: `python manage.py migrate`
    5. Start the development server: `python manage.py runserver`

    ## API Usage

    - Fetch FAQs in English (default): `curl http://localhost:8000/api/faqs/`
    - Fetch FAQs in Hindi: `curl http://localhost:8000/api/faqs/?lang=hi`
    - Fetch FAQs in Bengali: `curl http://localhost:8000/api/faqs/?lang=bn`

    ## Running Tests

    Run tests with: `pytest`

    ## Contribution Guidelines

    - Following PEP8 standards.
    - Written clear and concise commit messages.
