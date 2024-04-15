<div align="center">
<h1>Django Portfolio Project</h1>

> Still in Development

[View Project online](https://django-portfolio-project-dsx1.onrender.com/)

</div>

</br>

<details>
<summary>Project Deployment Guide</summary>

## Project deployment:

- Add those in requirements.txt
    ```text
    Django==5.0.4
    gunicorn==21.2.0
    pillow==10.3.0
    whitenoise==6.6.0
    ```
- Go to `settings.py` and modify as below:
    ```python
    DEBUG = True # making it False make the static file gone; I have to investigate more on it.
    ALLOWED_HOSTS = ["*"] # This can be also set as default domain after deployment
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic', # This must be added before 'django.contrib.staticfiles'
        'django.contrib.staticfiles',
        'portfolioapp',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', # This must be added here after SecurityMiddleware & SessionMiddleware
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    # Add those at the end
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
    ```
- Now go to render and select web service from New
- Select Github repo of the project
- Now in project setting page write Project Name (unique)
- Select Region, Branch
- Set Build command `pip install -r requirements.txt`
- Set start command `gunicorn portfolio.wsgi:application` # here portfolio is the project name
- Choose Instance Type `Free` and start deploy.

</details>

<details>
<summary>Features</summary>

## Features
- Currently user can add or modify frontend data from admin page
    - Navigate to [Admin Site](https://django-portfolio-project-dsx1.onrender.com/admin/)
    - `username: aatansen` ; `password: 123`

</details>