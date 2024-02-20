"""Add PreviewFile.width and PreviewFile.height

Revision ID: ae0127f2fc56
Revises: f5bdca075cdc
Create Date: 2023-09-13 17:22:11.318041

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "ae0127f2fc56"
down_revision = "f5bdca075cdc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("preview_file", schema=None) as batch_op:
        batch_op.add_column(sa.Column("width", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("height", sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("preview_file", schema=None) as batch_op:
        batch_op.drop_column("height")
        batch_op.drop_column("width")

    # ### end Alembic commands ###
