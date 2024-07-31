"""new table user new

Revision ID: e53d55a95921
Revises: cb8154d9b6e6
Create Date: 2024-07-24 18:19:49.872169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'e53d55a95921'
down_revision: Union[str, None] = 'cb8154d9b6e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
