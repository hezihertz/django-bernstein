import os
import sys	

path = '/var/www/django'
if path not in sys.path:
	sys.path.insert(0, path)
path = '/usr/local/lib/python2.7/site-packages/'
if path not in sys.path:
	sys.path.insert(1, path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bernstein.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
