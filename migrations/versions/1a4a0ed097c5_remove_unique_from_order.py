"""Remove unique from order

Revision ID: 1a4a0ed097c5
Revises: 821be02b5fb9
Create Date: 2021-10-28 18:59:31.599549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a4a0ed097c5'
down_revision = '821be02b5fb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('meal_order_key', 'meal', type_='unique')
    op.drop_constraint('meal_category_order_key', 'meal_category', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('meal_category_order_key', 'meal_category', ['order'])
    op.create_unique_constraint('meal_order_key', 'meal', ['order'])
    # ### end Alembic commands ###