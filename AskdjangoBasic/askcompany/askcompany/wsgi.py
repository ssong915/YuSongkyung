"""
WSGI config for askcompany project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askcompany.settings.prob') #진입점 (더 추가하고싶다면 그대로 (+import django) 다른 곳에도 선언가능)

application = get_wsgi_application()
