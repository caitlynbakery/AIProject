from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('MY_DEBUG', default=False, cast=bool)