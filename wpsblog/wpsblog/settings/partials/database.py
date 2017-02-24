import os
from .base import BASE_DIR

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#dj-database-url
#https://github.com/kennethreitz/dj-database-url
import dj_database_url

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'puzzle',
#         'USER': 'puzzle',
#         'PASSWORD': 'puzzle',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


DATABASES = {}
DATABASES['default'] = dj_database_url.config(default=os.environ.get("DATABASE_URL"),)