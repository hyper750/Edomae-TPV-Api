"""empty message

Revision ID: 664e0ea7edcb
Revises: e4f74b5818c6
Create Date: 2021-10-23 15:20:29.342260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664e0ea7edcb'
down_revision = 'e4f74b5818c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meal', sa.Column('imatge', sa.String(length=250), nullable=False))
    op.drop_column('meal', 'imatge_name')
    op.add_column('meal_category', sa.Column('imatge', sa.String(length=250), nullable=False))
    op.drop_column('meal_category', 'imatge_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meal_category', sa.Column('imatge_name', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
    op.drop_column('meal_category', 'imatge')
    op.add_column('meal', sa.Column('imatge_name', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
    op.drop_column('meal', 'imatge')
    # ### end Alembic commands ###
