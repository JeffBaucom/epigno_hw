"""empty message

Revision ID: 2965a6888e31
Revises: 
Create Date: 2018-04-23 15:25:20.011467

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2965a6888e31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operations_local',
    sa.Column('operation_id', sa.String(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('patient_age', sa.Integer(), nullable=True),
    sa.Column('operation_type_code', sa.String(), nullable=True),
    sa.Column('operation_entry_time', sa.DateTime(), nullable=True),
    sa.Column('operation_leave_time', sa.DateTime(), nullable=True),
    sa.Column('operation_start_time', sa.DateTime(), nullable=True),
    sa.Column('operation_end_time', sa.DateTime(), nullable=True),
    sa.Column('operation_room_code', sa.String(), nullable=True),
    sa.Column('surgeon_code', sa.String(), nullable=True),
    sa.Column('surgeon_assistant_code', sa.String(), nullable=True),
    sa.Column('surgeon_anesthesiologist_code', sa.String(), nullable=True),
    sa.Column('surgeon_scrub_nurse_code', sa.String(), nullable=True),
    sa.Column('surgeon_circulating_nurse_code', sa.String(), nullable=True),
    sa.Column('patient_gender_code', postgresql.ENUM('M', 'F', name='gender_types'), nullable=True),
    sa.PrimaryKeyConstraint('operation_id')
    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations_local')
    # ### end Alembic commands ###


def upgrade_hospital():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operations_hospital',
    sa.Column('operation_id', sa.String(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('patient_age', sa.Integer(), nullable=True),
    sa.Column('patient_gender_code', sa.Enum('M', 'F', name='gender_types'), nullable=True),
    sa.Column('operation_type_code', sa.String(), nullable=True),
    sa.Column('operation_entry_time', sa.DateTime(), nullable=True),
    sa.Column('operation_leave_time', sa.DateTime(), nullable=True),
    sa.Column('operation_start_time', sa.DateTime(), nullable=True),
    sa.Column('operation_end_time', sa.DateTime(), nullable=True),
    sa.Column('operation_room_code', sa.String(), nullable=True),
    sa.Column('surgeon_code', sa.String(), nullable=True),
    sa.Column('surgeon_assistant_code', sa.String(), nullable=True),
    sa.Column('surgeon_anesthesiologist_code', sa.String(), nullable=True),
    sa.Column('surgeon_scrub_nurse_code', sa.String(), nullable=True),
    sa.Column('surgeon_circulating_nurse_code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('operation_id')
    )
    # ### end Alembic commands ###


def downgrade_hospital():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations_hospital')
    # ### end Alembic commands ###

