# Running Database Sync

Prerequisites:
* Redis installed
* Postgresql installed
* SQLite3 installed

1. ```pip install -r requirements.txt```

2. Ensure Postgres server is running, create new database `epigno_dev` or edit `web/config.py` settings for `SQLALCHEMY_DATABASE_URI` to match your database name

3. Upgrade database
```
cd web
python manage.py db upgarde
```

4. Run server from `web` directory with `gunicorn server:app` 

5. Run `rq worker` from `web` directory to start synchronizing from upstream database