from server import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

#from operation_local import OperationLocal
#from operation_remote import OperationRemote
