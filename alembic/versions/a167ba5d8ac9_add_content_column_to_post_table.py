"""add content column to post table

Revision ID: a167ba5d8ac9
Revises: 30886a3dc9cc
Create Date: 2023-02-12 22:12:17.453513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a167ba5d8ac9'
down_revision = '30886a3dc9cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
