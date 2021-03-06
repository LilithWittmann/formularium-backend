from settings.settings import *
from os import environ
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": environ.get("RDS_DB_HOST"),
        "NAME": environ.get("RDS_DB_NAME"),
        "USER": environ.get("RDS_DB_USER"),
        "PASSWORD": environ.get("RDS_DB_PASSWORD"),
    },
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

AWS_EB_DEFAULT_REGION = "eu-central-1"
# your aws access key id
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
# your aws access key
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
# queue name to use - queues that don't exist will be created automatically

SECRET_KEY = environ.get("DJANGO_SECRET_KEY")

STATIC_ROOT = "/static/"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_REGION_NAME = "eu-central-1"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
