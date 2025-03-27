"""add Department

Revision ID: 1cf9110d2412
Revises: d4fbde2b6831
Create Date: 2025-03-27 10:08:16.996488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cf9110d2412'
down_revision = 'd4fbde2b6831'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('departments',  # Change from 'department' to 'departments'
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('departments')  # Change from 'department' to 'departments'
