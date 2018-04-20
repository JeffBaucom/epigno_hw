from operation import Operation

class OperationRemote(Operation):
    __tablename__ = 'operations_hospital'
    __bind_key__ = 'hospital'
