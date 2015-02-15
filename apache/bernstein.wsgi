import os
import sys	

path = ['/var/www/django','/usr/local/lib/python2.7/site-packages/']
sys.path = path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bernstein.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
