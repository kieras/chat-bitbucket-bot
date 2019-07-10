import os
import confuse

appName = 'ChatBitbucketBot'
os.environ[appName.upper()+'DIR'] = '.'
CONFIG = confuse.Configuration(appName, __name__)
