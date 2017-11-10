# to allow api client save environment state to database.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# we use cache for fast sessions.
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_COOKIE_NAME = 'sid'
SESSION_COOKIE_AGE = 86400 * 60  # 2 months. Very important to remember users.
SESSION_CACHE_ALIAS = "default"
CSRF_USE_SESSIONS = True
