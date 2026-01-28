# YumFood

**YumFood** is an online food ordering platform inspired by Domino's. Customers can browse the menu, add items to cart, place orders, and leave reviews. Admins can manage the menu, view orders, and track statistics.

## Features

- User registration, login, logout with email verification
- Menu display with food images, search, filtering by category
- Cart system with add/remove/update functionality
- Place orders and track order history
- Rate and review ordered food items
- Special offers with discounts
- Admin dashboard for managing foods and orders
- API documentation via Swagger and Redoc

## Tech Stack

- **Backend:** Django, Django REST Framework, Djoser, Cloudinary
- **Database:** PostgreSQL
- **Authentication:** JWT
- **Static/Media Storage:** Whitenoise, Cloudinary
- **Deployment:** Vercel/Heroku/DigitalOcean

## Installation

```bash
# Clone the repository
git clone <your-repo-link>
cd YumFood

# Create virtual environment
python -m venv .yumfood_env
source .yumfood_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run server
python manage.py runserver
```