web: gunicorn --pythonpath wpsblog/ --bind :7513 --worker=3 wpsblog.wsgi
worker: celery --workdir=wpsblog/ --app=wpsblog.celery:app --concurrency=3 worker
flower: celery --workdir=wpsblog/ --app=wpsblog.celery:app flower

