"""Added table coordinates

Revision ID: 4cf81a73610f
Revises: d4f56f63c6aa
Create Date: 2021-12-09 18:27:12.651605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cf81a73610f'
down_revision = 'd4f56f63c6aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('table', sa.Column('x_coordinates', sa.Float(precision=2), nullable=False))
    op.add_column('table', sa.Column('y_coordinates', sa.Float(precision=2), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('table', 'y_coordinates')
    op.drop_column('table', 'x_coordinates')
    # ### end Alembic commands ###
