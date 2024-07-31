"""new table user

Revision ID: cb8154d9b6e6
Revises: 41d138a4ad7f
Create Date: 2024-07-24 18:13:18.350793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'cb8154d9b6e6'
down_revision: Union[str, None] = '41d138a4ad7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
