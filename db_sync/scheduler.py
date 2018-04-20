import time
import atexit
import hashlib
import multiprocessing

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from redis import Redis
from rq import Queue, Worker, Connection

redis = Redis()
listen = ['default']
q = Queue(connection=redis)


scheduler = BackgroundScheduler()

from models import db, operation_remote, operation_local



def enqueue_sync():
    result = q.enqueue(db_sync)

scheduler.add_job(
    func=enqueue_sync,
    trigger=IntervalTrigger(seconds=5),
    id='db_sync',
    name='Sync database every five seconds',
    replace_existing=True)

atexit.register(lambda: scheduler.shutdown())

def worker_start():
    with Connection(redis):
        worker = Worker(list(map(Queue, listen)))
        multiprocessing.Process(target=worker.work()).start()

def db_sync():
    remote_records = operation_remote.OperationRemote.query.all()
    local_records = operation_local.OperationLocal.query.all()
    diff_remote(remote_records)
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


def diff_remote(remote_records):
    for record in remote_records:
        filtered = operation_local.OperationLocal.query.filter_by(operation_id=record.operation_id).first()
        if not filtered: # Record needs to be cloned
            new_operation = clone_remote(record)
            db.session.add(new_operation)
        else: # Record has already been cloned
            # Compile object attributes (excluding those that don't change, like operation_id)
            local_list = [str(filtered.updated_on),
                str(filtered.operation_entry_time),
                str(filtered.operation_leave_time),
                str(filtered.operation_start_time),
                filtered.operation_room_code,
                filtered.surgeon_assistant_code,
                filtered.surgeon_anesthesiologist_code,
                filtered.surgeon_scrub_nurse_code,
                filtered.surgeon_circulating_nurse_code]

            remote_list = [str(record.updated_on), str(record.operation_entry_time), 
            str(record.operation_leave_time), str(record.operation_start_time),
            record.operation_room_code, record.surgeon_assistant_code,
            record.surgeon_anesthesiologist_code, record.surgeon_scrub_nurse_code,
            record.surgeon_circulating_nurse_code]

            local_str = (" ".join(local_list)).encode('utf-8')
            remote_str = (" ".join(remote_list)).encode('utf-8')

            remote_hash = hashlib.md5(remote_str).hexdigest()
            local_hash = hashlib.md5(local_str).hexdigest()
            # compare hashes and call update function
            if local_hash != remote_hash:
                update_local(record, filtered)

    db.session.commit()

def clone_remote(operation_remote):
    return operation_local.OperationLocal(operation_remote.operation_id, operation_remote.created_on, operation_remote.updated_on, operation_remote.patient_age, operation_remote.patient_gender_code, operation_remote.operation_type_code, operation_remote.operation_entry_time, operation_remote.operation_leave_time, operation_remote.operation_start_time, operation_remote.operation_end_time, operation_remote.operation_room_code, operation_remote.surgeon_code, operation_remote.surgeon_assistant_code, operation_remote.surgeon_anesthesiologist_code, operation_remote.surgeon_scrub_nurse_code, operation_remote.surgeon_circulating_nurse_code)

def update_local(operation_remote, operation_local):
    attr_list = ['updated_on', 'operation_entry_time', 
    'operation_leave_time', 'operation_start_time',
    'operation_room_code', 'surgeon_assistant_code',
    'surgeon_anesthesiologist_code', 'surgeon_scrub_nurse_code',
    'surgeon_circulating_nurse_code']
    for i in attr_list:
        if getattr(operation_remote, i) != getattr(operation_local, i):
            setattr(operation_local, i, getattr(operation_remote, i))
