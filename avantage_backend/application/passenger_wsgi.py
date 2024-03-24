# -*- coding: utf-8 -*-
import os, sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, settings.PROJECT_DIR)
sys.path.insert(
    1,
    settings.PROJECT_PACKAGES_DIR,
)
os.environ["DJANGO_SETTINGS_MODULE"] = "avantage_backend.application.settings"

application = get_wsgi_application()
