import os
from export_credentials import ExportCredentials

setup_creds = ExportCredentials().setup_environment()

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')
TARGET_ACCOUNT = 'chefsteps'
