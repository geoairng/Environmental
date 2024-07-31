"""new table

Revision ID: 261ad82bad6c
Revises: 0f6310aa934c
Create Date: 2024-07-24 17:54:59.887827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '261ad82bad6c'
down_revision: Union[str, None] = '0f6310aa934c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
