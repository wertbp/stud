import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'wertiolp',
        'NAME': 'students_db',
    }
}