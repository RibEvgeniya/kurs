"""1

Revision ID: dd55344e3235
Revises: 
Create Date: 2023-11-12 18:42:19.038889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd55344e3235'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('region',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('area', sa.String(length=50), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('first_name', sa.String(length=75), nullable=False),
                    sa.Column('last_name', sa.String(length=75), nullable=False),
                    sa.Column('middle_name', sa.String(length=75), nullable=True),
                    sa.Column('email', sa.String(length=320), nullable=False),
                    sa.Column('phone', sa.String(length=12), nullable=False),
                    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.Column('birthdate', sa.Date(), nullable=False),
                    sa.Column('polis', sa.String(length=75), nullable=False),
                    sa.Column('adress', sa.String(length=75), nullable=False),
                    sa.Column('med_data_id', sa.Integer(), nullable=False),
                    sa.Column('gender', sa.String(length=10), nullable=False),
                    sa.Column('region_id', sa.Integer(), nullable=False),
                    ##sa.ForeignKeyConstraint(['med_data_id'], ['med_data.id'], ),
                    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('analysis',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('blood', sa.String(length=20), nullable=True),
    sa.Column('sugar', sa.String(length=20), nullable=True),
    sa.Column('urin', sa.String(length=20), nullable=True),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hronolog_illness',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('illness',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('symptoms', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('med_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('blood_type', sa.String(length=75), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('norm_presure', sa.String(length=75), nullable=True),
    sa.Column('sugar', sa.String(length=75), nullable=True),
    sa.Column('analysis_id', sa.Integer(), nullable=False),
    sa.Column('hr_ill_id', sa.Integer(), nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['analysis_id'], ['analysis.id'], ),
    sa.ForeignKeyConstraint(['hr_ill_id'], ['hronolog_illness.id'], ),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medicine',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('desc', sa.String(length=1000), nullable=True),
    sa.Column('contraindications', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_patient_email'), 'patient', ['email'], unique=True)
    op.create_table('photos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('rentgen', sa.String(length=20), nullable=True),
    sa.Column('EKG', sa.String(length=20), nullable=True),
    sa.Column('fluragraf', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('policlinic_polis',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('polis', sa.String(length=75), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('procedure',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=75), nullable=True),
    sa.Column('desc', sa.String(length=1000), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('specialisation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('oklad', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('diagnos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('illness_id', sa.Integer(), nullable=False),
    sa.Column('medicine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['illness_id'], ['illness.id'], ),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicine.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=75), nullable=False),
    sa.Column('last_name', sa.String(length=75), nullable=False),
    sa.Column('middle_name', sa.String(length=75), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('specialisation_id', sa.Integer(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('salary', sa.Float(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
    sa.ForeignKeyConstraint(['specialisation_id'], ['specialisation.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_employee_email'), 'employee', ['email'], unique=True)
    op.create_table('reception',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_open', sa.Boolean(), nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_diagnos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.Column('diag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diag_id'], ['diagnos.id'], ),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['emp_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.Column('diag_id', sa.Integer(), nullable=False),
    sa.Column('proc_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diag_id'], ['diagnos.id'], ),
    sa.ForeignKeyConstraint(['emp_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.ForeignKeyConstraint(['proc_id'], ['procedure.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_open', sa.Boolean(), nullable=False),
    sa.Column('pat_id', sa.Integer(), nullable=False),
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('cabinet', sa.String(length=10), nullable=True),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['emp_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['pat_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('examination',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('outdoors', sa.Boolean(), nullable=False),
    sa.Column('desc', sa.String(length=1000), nullable=True),
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['result_id'], ['result.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('examination')
    op.drop_table('schedule')
    op.drop_table('result')
    op.drop_table('patient_employee')
    op.drop_table('patient_diagnos')
    op.drop_table('reception')
    op.drop_index(op.f('ix_employee_email'), table_name='employee')
    op.drop_table('employee')
    op.drop_table('diagnos')
    op.drop_table('specialisation')
    op.drop_table('region')
    op.drop_table('procedure')
    op.drop_table('policlinic_polis')
    op.drop_table('photos')
    op.drop_index(op.f('ix_patient_email'), table_name='patient')
    op.drop_table('patient')
    op.drop_table('medicine')
    op.drop_table('med_data')
    op.drop_table('illness')
    op.drop_table('hronolog_illness')
    op.drop_table('analysis')
    # ### end Alembic commands ###