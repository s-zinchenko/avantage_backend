import os, sys
site_user_root_dir = '/home/r/raigoreg/raigoreg.beget.tech/public_html'
sys.path.insert(0, site_user_root_dir + '/avantage_backend')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'avantage_backend.application.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
