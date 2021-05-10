"""add timesheets locked field to org

Revision ID: 6d7fa5a8e9a5
Revises: 8e4f39e321f4
Create Date: 2021-05-07 13:19:06.751710

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6d7fa5a8e9a5'
down_revision = '8e4f39e321f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organisation', sa.Column('timesheets_locked', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organisation', 'timesheets_locked')
    # ### end Alembic commands ###
