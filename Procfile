web: gunicorn --pythonpath fwpsblog / --bind :5736 --worker=3 wpsblog.wsgi
worker: celery --workdir=wpsblog/ --app=wpsblog.wpsblog:app --concurrency=3 worker
flower: celery --workdir=wpsblog/ --app=wpsblog.wpsblog:app flower

