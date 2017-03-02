from .partials import *

DEBUG = False

ALLOWED_HOSTS = ["*", ]


STATICFILES_STORAGE = 'wpsblog.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'