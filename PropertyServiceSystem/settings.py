from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-fi&l8c9c7k^)5q0#32n09bqrlas7ojza$d=wce8pa_@unid3)e'

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "corsheaders",
    'PropertyServiceApp',
    'graphene_django',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PropertyServiceSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PropertyServiceSystem.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "PropertyServiceSystem",
        "USER": "postgres",
        "PASSWORD": "Gharibabu",
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'PropertyServiceApp.User'

GRAPHENE = {
    "SCHEMA": "PropertyServiceApp.schema.schema"
}


CORS_ALLOWED_ORIGINS = [
    "http://192.168.75.203:8000",
    "http://192.168.75.202:3000",
    "http://10.0.0.168:3000",
    "http://localhost:3000",
]

# -------START TWILIO CLLING DETAILS--------
# Email_Id = "haricoolguys@gmail.com"
# Password = 'Gurugubelliharibabu@1'

# ACCOUNT_SECURITY_API_KEY='jK2XmffiPhfxnt4IZ11bP9iVoDF7viBi'
# TWILIO_ACCOUNT_SID='AC7baedae59c1e3bf954d236cee52e5827'
# TWILIO_AUTH_TOKEN='35eda9457a6e281f5cf873d509111144'
# TWILIO_VERIFICATION_SID='VA9febac4ba0792225410e787b0d6f96ad'

# RECOVERY_CODE = "FosW0ypW4hxKuiSnc-d-yoDLHTxiStCBbc8jHVpc"

# -------STOP TWILIO CLLING DETAILS--------


# APPEND_SLASH=False

# --------------------------------------------
# Email_Id = "iamhacke1r@gmail.com"

ACCOUNT_SECURITY_API_KEY = 'iWX0PRx2KrJ2krs6dVkwS0yaQDVAM8Sa'
TWILIO_ACCOUNT_SID = 'AC7d62bbb1670a2c9627c1579dcaa98fea'
TWILIO_AUTH_TOKEN = 'f7c084677acb9e5909b3a33ce7557a2c'
TWILIO_VERIFICATION_SID = 'VAe868ed63e07bc1f15786eae3a2c67ca5'
# -------------------------------------------------------
