import logging

DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432
DB_NAME = 'blog'
DB_HOST = "blog_db"
DB_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s ]- %(name)s: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'blog.log'
        },
    },
    'loggers': {
        'blog': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
    },
}
