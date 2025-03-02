"""Added residence column to students

Revision ID: 8454482410aa
Revises: c2929e1e5527
Create Date: 2025-03-02 22:46:43.341268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8454482410aa'
down_revision = 'c2929e1e5527'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('students', sa.Column('residence', sa.String(), nullable=True))



def downgrade() -> None:
    op.drop_column('students', 'email')

