"""create posts table

Revision ID: 28f4fb65ba8b
Revises: 
Create Date: 2022-08-03 10:18:13.652147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f4fb65ba8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts', 
        sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
        sa.Column('title', sa.String(), nullable = False)
        )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
