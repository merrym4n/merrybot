"""
WSGI config for bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

''''''
#Server
sys.path.append('/home/ubuntu/merrybot')
sys.path.append('/home/ubuntu/merrybot/myvenv/lib/python3.5/site-packages')
'''
#Develop
sys.path.append('/home/merryman/merrybot')
sys.path.append('/home/merryman/merrybot/myvenv/lib/python3.5/site-packages')
'''
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot.settings")

application = get_wsgi_application()
