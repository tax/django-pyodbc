import os

PASSWORD = os.environ.get('MSSQL_PASSWORD', 'myp@ssword')

DATABASES = {
    'default': {
        'ENGINE': "django_pyodbc",
        'HOST': "tcp:djangopyodbc.cloudapp.net,49544",
        'USER': "sa",
        'PASSWORD': PASSWORD,
        'NAME': "django_odbc_test",
        'OPTIONS': {
            'encoding': 'utf-8',
            'driver': "SQL Server Native Client 11.0",
            'autocommit': True,
        },
    },
    'other': {
        'ENGINE': "django_pyodbc",
        'HOST': "tcp:djangopyodbc.cloudapp.net,49544",
        'USER': "sa",
        'PASSWORD': PASSWORD,
        'NAME': "otherdb",
        'OPTIONS': {
            'encoding': 'utf-8',
            'driver': "SQL Server Native Client 11.0",
            'autocommit': True,
        },
    },
}
SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
