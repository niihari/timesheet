from os import environ


API_PORT = environ.get('API_PORT', default='1234')
DB_USER = environ.get('DB_USER', default='user')
DB_PASSWORD = environ.get('DB_PASSWORD', default='password')
DB_HOST = environ.get('DB_HOST', default='localhost')
DB_PORT = environ.get('DB_PORT', default='1337')
DB_INSTANCE = environ.get('DB_INSTANCE', default='postgres')
