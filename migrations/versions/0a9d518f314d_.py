"""empty message

Revision ID: 0a9d518f314d
Revises: e39abb71f343
Create Date: 2023-12-18 18:08:34.711133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a9d518f314d'
down_revision: Union[str, None] = 'e39abb71f343'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('product')
    op.add_column('operation', sa.Column('quantity', sa.String(), nullable=True))
    op.add_column('operation', sa.Column('figi', sa.String(), nullable=True))
    op.add_column('operation', sa.Column('instrument_type', sa.String(), nullable=True))
    op.add_column('operation', sa.Column('date', sa.TIMESTAMP(), nullable=True))
    op.drop_column('operation', 'name')
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    op.add_column('operation', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('operation', 'date')
    op.drop_column('operation', 'instrument_type')
    op.drop_column('operation', 'figi')
    op.drop_column('operation', 'quantity')
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('img', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('maker', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('characteristic', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    op.drop_table('role')
    # ### end Alembic commands ###