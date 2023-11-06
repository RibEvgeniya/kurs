"""5

Revision ID: 33f85b099754
Revises: 2f024971c8d5
Create Date: 2023-11-05 17:35:12.541267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33f85b099754'
down_revision: Union[str, None] = '2f024971c8d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('illness',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=75), nullable=True),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('med_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('blood_type', sa.String(length=75), nullable=True),
    sa.Column('height', sa.String(length=75), nullable=True),
    sa.Column('weight', sa.String(length=75), nullable=True),
    sa.Column('norm_presure', sa.String(length=75), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medicine',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=75), nullable=True),
    sa.Column('desc', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('policlinic_polis',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('polis', sa.String(length=75), nullable=False),
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
    sa.ForeignKeyConstraint(['illness_id'], ['illness.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('room')
    op.drop_table('post')
    op.drop_index('ix_pat_email', table_name='pat')
    op.drop_table('pat')
    op.add_column('employee', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.add_column('employee', sa.Column('region', sa.String(length=20), nullable=True))
    op.add_column('employee', sa.Column('specialisation_id', sa.Integer(), nullable=False))
    op.add_column('employee', sa.Column('birthdate', sa.Date(), nullable=False))
    op.add_column('employee', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.alter_column('employee', 'middle_name',
               existing_type=sa.VARCHAR(length=75),
               nullable=True)
    op.create_unique_constraint(None, 'employee', ['phone'])
    op.create_foreign_key(None, 'employee', 'specialisation', ['specialisation_id'], ['id'])
    op.add_column('patient', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('patient', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.add_column('patient', sa.Column('birthdate', sa.Date(), nullable=False))
    op.add_column('patient', sa.Column('polis', sa.String(length=75), nullable=False))
    op.add_column('patient', sa.Column('adress', sa.String(length=75), nullable=False))
    op.add_column('patient', sa.Column('med_data_id', sa.Integer(), nullable=False))
    op.alter_column('patient', 'middle_name',
               existing_type=sa.VARCHAR(length=75),
               nullable=True)
    op.create_foreign_key(None, 'patient', 'med_data', ['med_data_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.alter_column('patient', 'middle_name',
               existing_type=sa.VARCHAR(length=75),
               nullable=False)
    op.drop_column('patient', 'med_data_id')
    op.drop_column('patient', 'adress')
    op.drop_column('patient', 'polis')
    op.drop_column('patient', 'birthdate')
    op.drop_column('patient', 'is_verified')
    op.drop_column('patient', 'is_superuser')
    op.drop_constraint(None, 'employee', type_='foreignkey')
    op.drop_constraint(None, 'employee', type_='unique')
    op.alter_column('employee', 'middle_name',
               existing_type=sa.VARCHAR(length=75),
               nullable=False)
    op.drop_column('employee', 'is_superuser')
    op.drop_column('employee', 'birthdate')
    op.drop_column('employee', 'specialisation_id')
    op.drop_column('employee', 'region')
    op.drop_column('employee', 'is_verified')
    op.create_table('pat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=75), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=75), autoincrement=False, nullable=False),
    sa.Column('middle_name', sa.VARCHAR(length=75), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=320), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('birthdate', sa.DATE(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pat_pkey')
    )
    op.create_index('ix_pat_email', 'pat', ['email'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='post_pkey'),
    sa.UniqueConstraint('name', name='post_name_key')
    )
    op.create_table('room',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type_room', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('area', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('max_quest', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='room_pkey')
    )
    op.drop_table('diagnos')
    op.drop_table('specialisation')
    op.drop_table('policlinic_polis')
    op.drop_table('patient_employee')
    op.drop_table('medicine')
    op.drop_table('med_data')
    op.drop_table('illness')
    # ### end Alembic commands ###