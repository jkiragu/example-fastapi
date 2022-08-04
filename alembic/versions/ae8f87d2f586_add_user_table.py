"""Add user table

Revision ID: ae8f87d2f586
Revises: 8036578078d9
Create Date: 2022-08-03 14:38:44.429657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae8f87d2f586'
down_revision = '8036578078d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable = False),
        sa.Column('email', sa.String(), nullable = False),
        sa.Column('password', sa.String(), nullable = False),
        sa.Column('created_at', sa.TIMESTAMP(timezone = True), server_default = sa.text('now()'), nullable = False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
