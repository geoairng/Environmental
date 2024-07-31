"""one more

Revision ID: ee467b23fd2b
Revises: 53f3dcf310d5
Create Date: 2024-07-24 18:51:16.055886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ee467b23fd2b'
down_revision: Union[str, None] = '53f3dcf310d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
