"""Add created and indeces

Revision ID: 775376f4a90f
Revises: 33aafc656715
Create Date: 2025-10-24 10:56:52.999581

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "775376f4a90f"
down_revision: Union[str, Sequence[str], None] = "33aafc656715"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("requests", sa.Column("created", sa.DateTime(), nullable=False))
    op.alter_column(
        "requests", "request_url", existing_type=sa.VARCHAR(), nullable=False
    )
    op.create_index(op.f("ix_requests_created"), "requests", ["created"], unique=False)
    op.create_index(op.f("ix_requests_user_id"), "requests", ["user_id"], unique=False)
    op.add_column("users", sa.Column("created", sa.DateTime(), nullable=True))
    op.alter_column("users", "user_uuid", existing_type=sa.VARCHAR(), nullable=False)
    op.create_index(op.f("ix_users_user_uuid"), "users", ["user_uuid"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_users_user_uuid"), table_name="users")
    op.alter_column("users", "user_uuid", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_column("users", "created")
    op.drop_index(op.f("ix_requests_user_id"), table_name="requests")
    op.drop_index(op.f("ix_requests_created"), table_name="requests")
    op.alter_column(
        "requests", "request_url", existing_type=sa.VARCHAR(), nullable=True
    )
    op.drop_column("requests", "created")
