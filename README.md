# 🏠 Apartments site

Django SECRET_KEY and YMAPS_API_KEY are stored in environment variables.

-----

## 🖼 Preview

## 🔧 Setup
```bash
git clone https://github.com/lep0n/apartments-site.git

cd apartments-site/

pipenv shell

pipenv install --ignore-pipfile

cd app/

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```