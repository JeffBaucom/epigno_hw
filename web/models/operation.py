import enum
from . import db


class Operation(db.Model):
    __abstract__ = 1
    __tablename__ = 'operations'

    operation_id = db.Column(db.String(), primary_key=True)
    created_on = db.Column(db.DateTime())
    updated_on = db.Column(db.DateTime())
    patient_age = db.Column(db.Integer)
    patient_gender_code = db.Column(
        db.Enum("M", "F", name="gender_types", create_type=False,
                checkfirst=True))
    operation_type_code = db.Column(db.String())
    operation_entry_time = db.Column(db.DateTime())
    operation_leave_time = db.Column(db.DateTime())
    operation_start_time = db.Column(db.DateTime())
    operation_end_time = db.Column(db.DateTime())
    operation_room_code = db.Column(db.String())
    surgeon_code = db.Column(db.String())
    surgeon_assistant_code = db.Column(db.String())
    surgeon_anesthesiologist_code = db.Column(db.String())
    surgeon_scrub_nurse_code = db.Column(db.String())
    surgeon_circulating_nurse_code = db.Column(db.String())

    def __init__(self, operation_id, created_on, updated_on, patient_age,
                 patient_gender_code, operation_type_code, operation_entry_time,
                 operation_leave_time, operation_start_time, operation_end_time,
                 operation_room_code, surgeon_code, surgeon_assistant_code,
                 surgeon_anesthesiologist_code, surgeon_scrub_nurse_code,
                 surgeon_circulating_nurse_code):
        self.operation_id = operation_id
        self.created_on = created_on
        self.updated_on = updated_on
        self.patient_age = patient_age
        self.patient_gender_code = patient_gender_code
        self.operation_type_code = operation_type_code
        self.operation_entry_time = operation_entry_time
        self.operation_leave_time = operation_leave_time
        self.operation_start_time = operation_start_time
        self.operation_end_time = operation_end_time
        self.operation_room_code = operation_room_code
        self.surgeon_code = surgeon_code
        self.surgeon_assistant_code = surgeon_assistant_code
        self.surgeon_anesthesiologist_code = surgeon_anesthesiologist_code
        self.surgeon_scrub_nurse_code = surgeon_scrub_nurse_code
        self.surgeon_circulating_nurse_code = surgeon_circulating_nurse_code

    def __repr__(self):
        return '<id {}>'.format(self.operation_id)


class OperationRemote(Operation):
    __tablename__ = 'operations_hospital'
    __bind_key__ = 'hospital'
