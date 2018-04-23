from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


db_sync_blueprint = Blueprint('db_sync', __name__, template_folder='templates')

@db_sync_blueprint.record
def record(state):
    from db_sync import scheduler
    scheduler.scheduler.start()
    #if __name__ == '__main__':
    #scheduler.worker_start()

@db_sync_blueprint.route('/', defaults={'page': 'index'})
@db_sync_blueprint.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
