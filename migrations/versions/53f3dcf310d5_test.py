"""test

Revision ID: 53f3dcf310d5
Revises: e53d55a95921
Create Date: 2024-07-24 18:30:25.754704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '53f3dcf310d5'
down_revision: Union[str, None] = 'e53d55a95921'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
