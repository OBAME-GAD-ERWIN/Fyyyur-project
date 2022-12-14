"""empty message

Revision ID: 656e34867607
Revises: cb91189107a9
Create Date: 2022-11-29 14:12:12.961678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '656e34867607'
down_revision = 'cb91189107a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))

    with op.batch_alter_table('venues', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venues', schema=None) as batch_op:
        batch_op.drop_column('genres')

    with op.batch_alter_table('artists', schema=None) as batch_op:
        batch_op.drop_column('genres')

    # ### end Alembic commands ###
