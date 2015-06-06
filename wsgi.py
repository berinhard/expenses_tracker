
import os
import sys

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

project_path = os.path.join(os.path.dirname(__file__), 'project')
sys.path.insert(0, project_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = Cling(get_wsgi_application())
