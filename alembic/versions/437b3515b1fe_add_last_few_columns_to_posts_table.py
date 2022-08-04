"""Add last few columns to posts table

Revision ID: 437b3515b1fe
Revises: 2b0c0589dbba
Create Date: 2022-08-03 15:20:19.361596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '437b3515b1fe'
down_revision = '2b0c0589dbba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
