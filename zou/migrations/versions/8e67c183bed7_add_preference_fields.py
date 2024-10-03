"""add prefeence fields

Revision ID: 8e67c183bed7
Revises: 59a7445a966c
Create Date: 2024-09-26 10:48:45.678791

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '8e67c183bed7'
down_revision = '59a7445a966c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('organisation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dark_theme_by_default', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('format_duration_in_hours', sa.Boolean(), nullable=True))

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_publish_default_for_artists', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('hd_bitrate_compression', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('ld_bitrate_compression', sa.Integer(), nullable=True))

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('difficulty', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('difficulty')

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('ld_bitrate_compression')
        batch_op.drop_column('hd_bitrate_compression')
        batch_op.drop_column('is_publish_default_for_artists')

    with op.batch_alter_table('organisation', schema=None) as batch_op:
        batch_op.drop_column('format_duration_in_hours')
        batch_op.drop_column('dark_theme_by_default')

    # ### end Alembic commands ###
