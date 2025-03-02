"""Renaming students to scholars

Revision ID: c2929e1e5527
Revises: 791279dd0760
Create Date: 2025-03-02 22:27:58.965144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2929e1e5527'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "scholars")


def downgrade() -> None:
    op.rename_table("scholars", "students")

