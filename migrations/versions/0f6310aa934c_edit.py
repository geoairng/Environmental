"""edit

Revision ID: 0f6310aa934c
Revises: 63e74a1002c1
Create Date: 2024-07-24 17:49:21.627120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0f6310aa934c'
down_revision: Union[str, None] = '63e74a1002c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
