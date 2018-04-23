from . import operation


class OperationRemote(operation.Operation):
    __tablename__ = 'operations_hospital'
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'hospital'
