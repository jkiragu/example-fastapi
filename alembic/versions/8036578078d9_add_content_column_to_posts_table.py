"""add content column to posts table

Revision ID: 8036578078d9
Revises: 28f4fb65ba8b
Create Date: 2022-08-03 10:28:01.783893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8036578078d9'
down_revision = '28f4fb65ba8b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
