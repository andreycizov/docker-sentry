import os, os.path

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE','django.db.backends.postgresql_psycopg2'),  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.getenv('DB_NAME','docker'),               # Or path to database file if using sqlite3.
        'USER': os.getenv('DB_USER', 'docker'),                        # Not used with sqlite3.
        'PASSWORD': os.getenv('DB_PASSWORD', 'docker'),                    # Not used with sqlite3.
        'HOST': os.getenv('DB_HOST', 'docker'),                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': os.getenv('DB_PORT', ''),                              # Set to empty string for default. Not used with sqlite3.
    }
}

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

###########
## CACHE ##
###########

# You'll need to install the required dependencies for Memcached:
#   pip install python-memcached
#
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['memcached:11211'],
    }
}

###########
## Queue ##
###########

# See http://sentry.readthedocs.org/en/latest/queue/index.html for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

# You can enable queueing of jobs by turning off the always eager setting:
CELERY_ALWAYS_EAGER = False
BROKER_URL = 'amqp://guest:guest@ampq:5672//'

####################
## Update Buffers ##
####################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

# You'll need to install the required dependencies for Redis buffers:
#   pip install redis hiredis nydus
#
SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': 'redis',
            'port': 6379,
        }
    }
}

################
## Web Server ##
################


SENTRY_KEY = os.getenv('SENTRY_KEY', '333dkdslyvBUGWq5bcnW9d1MZQ82qmPZB4pskKS3223fdBfuhySw==')

# Set this to false to require authentication
SENTRY_PUBLIC = False

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!

SENTRY_WEB_HOST = os.getenv("WEB_HOST", '0.0.0.0')
SENTRY_WEB_PORT = int(os.getenv("WEB_PORT", '80'))
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
}
# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''