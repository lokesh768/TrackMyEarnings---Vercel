from django.core.wsgi import get_wsgi_application
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrackMyEarnings.settings")
django.setup()
application = get_wsgi_application()
