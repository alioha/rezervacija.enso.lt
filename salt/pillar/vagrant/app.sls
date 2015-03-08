app:
  path: /srv/src
  uwsgi_module: app.wsgi:application
  uwsgi_logs: /var/log/uwsgi/app.log
  db_user: django
  db_password: django2235
  db_name: django_db
