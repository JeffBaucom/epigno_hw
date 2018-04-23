import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import redis
from rq import Connection, Worker

from server import app
from models import db

app.config.from_object('config.Config')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def runworker():
    redis_url = app.config['REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config['QUEUES'])
        worker.work()


if __name__ == '__main__':
    manager.run()
