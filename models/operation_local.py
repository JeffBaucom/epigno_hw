from operation import Operation
from sqlalchemy.dialects.postgresql import ENUM
from . import db

class OperationLocal(Operation):
    __tablename__ = 'operations_local'
    __bind_key__ = None
    patient_gender_code = db.Column(ENUM("M", "F", name="gender_types", create_type=False))
