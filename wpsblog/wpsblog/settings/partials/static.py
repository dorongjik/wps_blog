import os
from .base import PROJECT_ROOT_DIR
from .base import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


# 개발 단계에서는 이곳을 찾음 (Debug = True 를 기준으로 판단)
STATICFILES_DIR = [
    os.path.join(BASE_DIR, "wpsblog", "static")
]

STATIC_URL = '/static/'

# 배포 단계에서는 이곳을 찾음
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")


STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'wpsblog': {
            'source_filenames': (
              'plugins/jquery-ui/jquery-ui.css',
              'plugins/bootstrap/css/bootstrap.min.css',
              'plugins/font-awesome/css/font-awesome.min.css',
              'plugins/selectbox/select_option1.css',
              'plugins/rs-plugin/css/settings.css',
              'plugins/owl-carousel/owl.carousel.css',
              
              'https://fonts.googleapis.com/css?family=Oxygen:400,300,700',

              'css/style.css',
              'css/colors/default.css',

            ),
            'output_filename': 'css/wpsblog.css',
        }
    },

    'JAVASCRIPT': {
        'script': {
            'source_filenames': (
              'https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js',
              
              'plugins/jquery-ui/jquery-ui.js',
              'plugins/bootstrap/js/bootstrap.min.js',
              'plugins/rs-plugin/js/jquery.themepunch.tools.min.js',
              'plugins/rs-plugin/js/jquery.themepunch.revolution.min.js',
              'plugins/owl-carousel/owl.carousel.js',
              'plugins/selectbox/jquery.selectbox-0.1.3.min.js',
              'plugins/countdown/jquery.syotimer.js',

              'js/custom.js',
            ),
            'output_filename': 'js/stats.js',
        }
    },
}

# MEDIA

MEDIA_ROOT = os.path.join(
    PROJECT_ROOT_DIR,
    "dist",
    "media",
)

MEDIA_URL = '/media/'
