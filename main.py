import os
from export_credentials import ExportCredentials
from insta_follower import InstaFollower

setup_creds = ExportCredentials().setup_environment()

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')
TARGET_ACCOUNT = 'chefsteps'

instaFollower = InstaFollower()
instaFollower.login()
instaFollower.find_followers()
instaFollower.follow()
