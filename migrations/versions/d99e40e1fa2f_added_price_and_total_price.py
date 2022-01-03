"""Added price and total price

Revision ID: d99e40e1fa2f
Revises: 7d64233f6298
Create Date: 2022-01-03 01:02:18.490343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99e40e1fa2f'
down_revision = '7d64233f6298'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('command_meal', sa.Column('price', sa.Float(precision=2), nullable=False))
    op.add_column('command_meal', sa.Column('total_price', sa.Float(precision=2), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('command_meal', 'total_price')
    op.drop_column('command_meal', 'price')
    # ### end Alembic commands ###