"""create prompt table

Revision ID: 9fd7ee516968
Revises: 
Create Date: 2024-03-31 18:05:04.521248

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9fd7ee516968"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "prompt",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.Unicode(256), nullable=False),
        sa.Column("text", sa.Unicode(4096), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("prompt")
