import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Amazon S3 setting
# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = 'connectedworld_static'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = DEFAULT_FILE_STORAGE

# URL prefix for static files.
# STATIC_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/'

# Unique key for Django.
SECRET_KEY = os.environ.get('SECRET_KEY')

# RabbitMQ
# BROKER_URL = os.environ.get('CLOUDAMQP_URL')

# Memcache
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

# Cache settings
CACHES = {
 	'default': {
		'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
		'LOCATION': os.environ.get('MEMCACHIER_SERVERS', ''),
		'TIMEOUT': 500,
		'BINARY': True,
	}
}