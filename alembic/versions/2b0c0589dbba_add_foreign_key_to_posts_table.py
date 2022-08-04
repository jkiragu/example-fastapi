"""Add foreign key to posts table

Revision ID: 2b0c0589dbba
Revises: ae8f87d2f586
Create Date: 2022-08-03 15:15:21.100100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b0c0589dbba'
down_revision = 'ae8f87d2f586'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table = "posts", referent_table = "users", local_cols = ['owner_id'], remote_cols = ['id'], ondelete = "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name = 'posts')
    op.drop_column('posts', 'owner_id')
    pass
