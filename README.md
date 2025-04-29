# MyApp

A Django project with static and media file handling, environment variable support, and extended app structure.

## 🚀 Features

- Django backend setup
- Static and media file configuration
- Environment variables using `python-decouple`
- Template and static files managed within app
- Extended app structure for frontend integration

## 📁 Project Structure

myproject/ ├── myapp/ │ ├── templates/ │ ├── static/ │ └── ... ├── static/ ├── media/ ├── .env ├── .gitignore ├── manage.py ├── requirements.txt └── README.md

bash
Copy
Edit

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Create virtual environment and activate

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Environment Variables

Create a .env file in the root directory and add:

ini
Copy
Edit
SECRET_KEY=your_secret_key
DEBUG=True
Run migrations and start server

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Access Open http://127.0.0.1:8000/ in your browser.

📝 Notes
Media and static files are served via development server using:

python
Copy
Edit
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Sensitive files like .env, venv/, media/, __pycache__/ are excluded using .gitignore.

📦 External Packages Used
python-decouple — for environment variable management