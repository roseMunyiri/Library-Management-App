"""Remove 'pages' column from Book model

Revision ID: 985a9cfdddd3
Revises: 
Create Date: 2023-09-14 21:16:13.685871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985a9cfdddd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_column('pages')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pages', sa.INTEGER(), nullable=False))

    # ### end Alembic commands ###
