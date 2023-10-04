"""Recreate books table with Quantity column as NOT NULL

Revision ID: 6c254e8ea735
Revises: b0e690cdedfe
Create Date: 2023-09-17 12:09:35.814719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c254e8ea735'
down_revision = 'b0e690cdedfe'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
op.create_table(
    'books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=False),
    sa.Column('isbn', sa.String(length=20), nullable=False),
    sa.Column('publisher', sa.String(length=150), nullable=False),
    sa.Column('Quantity', sa.Integer(), nullable=False, server_default='0'),  # Add this line
    sa.PrimaryKeyConstraint('id')
)
