"""
WSGI config for newsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('/home/pratyush/Desktop/NewsSite/NewsSite/newsite')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsite.settings')

application = get_wsgi_application()
os.environ['http_proxy'] = "http://myproxy:port"
os.environ['https_proxy'] = "http://myproxy:port"