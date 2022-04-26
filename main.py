import os
from export_credentials import ExportCredentials
from insta_follower import InstaFollower

setup_creds = ExportCredentials().setup_environment()

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')

instaFollower = InstaFollower()
instaFollower.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
instaFollower.find_followers()
instaFollower.follow()
