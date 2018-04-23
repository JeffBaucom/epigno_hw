from flask import Flask
import os

app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#==============================================================================
# Comment these lines to remove syncronization from app
#==============================================================================
from db_sync.views import db_sync_blueprint
app.register_blueprint(db_sync_blueprint)
#==============================================================================

@app.route('/')
def hello_world():
    return 'Hello, World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
