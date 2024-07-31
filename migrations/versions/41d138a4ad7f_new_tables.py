"""new tables

Revision ID: 41d138a4ad7f
Revises: 5123eed54bec
Create Date: 2024-07-24 18:06:11.907628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '41d138a4ad7f'
down_revision: Union[str, None] = '5123eed54bec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
