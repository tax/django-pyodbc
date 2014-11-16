# This is an example test settings file for use with the Django test suite.
#
# The 'sqlite3' backend requires only the ENGINE setting (an in-
# memory database will be used). All other backends will require a
# NAME and potentially authentication information. See the
# following section in the docs for more information:
#
# https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
#
# The different databases that Django supports behave differently in certain
# situations, so it is recommended to run the test suite against as many
# database backends as possible.  You may want to create a separate settings
# file for each of the backends you test against.
import os

PASSWORD = os.environ.get('MSSQL_PASSWORD', 'myp@ssword')

DATABASES = {
    'default': {
        'ENGINE': "django_pyodbc",
        'HOST': "djangopyodbc.cloudapp.net",
        'USER': "sa",
        'PASSWORD': PASSWORD,
        'NAME': "django_odbc_test",
        'OPTIONS': {
            'host_is_server': True,
            'extra_params': 'DATABASE=django_odbc_test;Port=49544;',
            'encoding': 'utf-8',
            'driver': "FreeTDS",
        },
    },
    'other': {
        'ENGINE': "django_pyodbc",
        'HOST': "djangopyodbc.cloudapp.net",
        'USER': "sa",
        'PASSWORD': PASSWORD,
        'NAME': "otherdb",
        'OPTIONS': {
            'host_is_server': True,
            'extra_params': 'DATABASE=otherdb;Port=49544;',
            'encoding': 'utf-8',
            'driver': "FreeTDS",
        },
    },
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
