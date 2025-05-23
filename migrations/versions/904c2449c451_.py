"""empty message

Revision ID: 904c2449c451
Revises: 171dde873006
Create Date: 2025-04-23 10:19:31.766232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '904c2449c451'
down_revision = '171dde873006'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firts_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('second_name', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('second_name')
        batch_op.drop_column('firts_name')

    # ### end Alembic commands ###
