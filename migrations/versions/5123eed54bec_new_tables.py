"""new tables

Revision ID: 5123eed54bec
Revises: 261ad82bad6c
Create Date: 2024-07-24 17:58:04.105055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '5123eed54bec'
down_revision: Union[str, None] = '261ad82bad6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
