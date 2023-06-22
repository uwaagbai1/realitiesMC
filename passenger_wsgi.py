import sys
import os

# Add the directory containing your project to the sys.path
sys.path.append('/home/realiti3/public_html/realitiesMC')

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Import the WSGI application object from your project's wsgi.py file
from config.wsgi import application