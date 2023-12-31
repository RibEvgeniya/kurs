"""2

Revision ID: a585c66f03ee
Revises: dd55344e3235
Create Date: 2023-11-12 19:22:27.208989

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a585c66f03ee'
down_revision: Union[str, None] = 'dd55344e3235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'is_superuser')
    op.drop_column('patient', 'med_data_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('med_data_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('employee', sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
