"""baseline schema

Revision ID: 3395c987322e
Revises: 
Create Date: 2025-10-26 17:49:52.476850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3395c987322e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "members",
        sa.Column("member_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False, unique=True),
    )

    op.create_table(
        "books",
        sa.Column("book_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("author", sa.String, nullable=False),
        sa.Column("is_borrowed", sa.Boolean, nullable=False, server_default=sa.text("false")),
        sa.Column("borrowed_date", sa.Date, nullable=True, server_default=None),
        sa.Column("borrowed_by", sa.Integer, nullable=True, server_default=None),
    )

def downgrade() -> None:
    op.drop_table("books")
    op.drop_table("members")
