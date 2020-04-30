import os

APP_ENV = os.getenv('APP_ENV')
if APP_ENV == 'prod':
    from comicfun.env.setting_prod import *
elif APP_ENV == 'test':
    from comicfun.env.setting_test import *
elif APP_ENV == 'dev':
    from comicfun.env.setting_dev import *
else:
    from comicfun.env.setting_dev import *
