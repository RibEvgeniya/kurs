"""5

Revision ID: 6ea36d77c528
Revises: e9a04f35b4f9
Create Date: 2023-11-12 20:32:27.712324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ea36d77c528'
down_revision: Union[str, None] = 'e9a04f35b4f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blank',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('blank', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('rentgen', sa.String(length=20), nullable=True),
    sa.Column('EKG', sa.String(length=20), nullable=True),
    sa.Column('fluragraf', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('photos')
    op.add_column('analysis', sa.Column('photo_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'analysis', 'photo', ['photo_id'], ['id'])
    op.add_column('employee', sa.Column('education', sa.String(length=320), nullable=False))
    op.add_column('employee', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.create_index(op.f('ix_employee_education'), 'employee', ['education'], unique=True)
    op.add_column('examination', sa.Column('diagnos_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'examination', 'diagnos', ['diagnos_id'], ['id'])
    op.add_column('illness', sa.Column('MKB10_code', sa.String(length=10), nullable=True))
    op.add_column('illness', sa.Column('treatment', sa.String(length=200), nullable=True))
    op.add_column('medicine', sa.Column('producer', sa.String(length=50), nullable=True))
    op.add_column('medicine', sa.Column('release_form', sa.String(length=1000), nullable=True))
    op.add_column('patient', sa.Column('region_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'patient', 'region', ['region_id'], ['id'])
    op.add_column('procedure', sa.Column('indications', sa.String(length=1000), nullable=True))
    op.add_column('procedure', sa.Column('contraindications', sa.String(length=1000), nullable=True))
    op.add_column('result', sa.Column('res_price', sa.Float(), nullable=True))
    op.add_column('specialisation', sa.Column('procedure_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'specialisation', 'procedure', ['procedure_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'specialisation', type_='foreignkey')
    op.drop_column('specialisation', 'procedure_id')
    op.drop_column('result', 'res_price')
    op.drop_column('procedure', 'contraindications')
    op.drop_column('procedure', 'indications')
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'region_id')
    op.drop_column('medicine', 'release_form')
    op.drop_column('medicine', 'producer')
    op.drop_column('illness', 'treatment')
    op.drop_column('illness', 'MKB10_code')
    op.drop_constraint(None, 'examination', type_='foreignkey')
    op.drop_column('examination', 'diagnos_id')
    op.drop_index(op.f('ix_employee_education'), table_name='employee')
    op.drop_column('employee', 'is_superuser')
    op.drop_column('employee', 'education')
    op.drop_constraint(None, 'analysis', type_='foreignkey')
    op.drop_column('analysis', 'photo_id')
    op.create_table('photos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('desc', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('rentgen', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('EKG', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('fluragraf', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='photos_pkey')
    )
    op.drop_table('photo')
    op.drop_table('blank')
    # ### end Alembic commands ###
