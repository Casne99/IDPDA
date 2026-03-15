"""add blacklist table

Revision ID: 20260315_add_blacklist
Revises: 20260307_auto_credentials
Create Date: 2026-03-15

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20260315_add_blacklist'
down_revision = '20260307_auto_credentials'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'blacklist',
        sa.Column('user', sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(['user'], ['credentials.user']),
        sa.PrimaryKeyConstraint('user')
    )


def downgrade() -> None:
    op.drop_table('blacklist')
