"""
WSGI config for {{ project_name }} project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os

# For venv
# import sys
# python_home = '/opt/venv/exam'
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
# activate_this = python_home + '/bin/activate_this.py'
# exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()

# Wrap werkzeug debugger if DEBUG is on
if settings.DEBUG:
    try:
        import django.views.debug
        import six
        from werkzeug.debug import DebuggedApplication

        def null_technical_500_response(request, exc_type, exc_value, tb):
            six.reraise(exc_type, exc_value, tb)

        django.views.debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True,
                                          # Turning off pin security as DEBUG is True
                                          pin_security=False)
    except ImportError:
        pass
