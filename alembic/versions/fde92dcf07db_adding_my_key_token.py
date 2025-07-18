"""adding my key token

Revision ID: fde92dcf07db
Revises: 03ff80d79056
Create Date: 2025-07-14 10:54:27.864258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fde92dcf07db'
down_revision: Union[str, None] = '03ff80d79056'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my-keys', sa.Column('user_token', sa.String(length=128), nullable=False))
    op.drop_index('ix_my-keys_key_value', table_name='my-keys')
    op.create_index(op.f('ix_my-keys_user_token'), 'my-keys', ['user_token'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_my-keys_user_token'), table_name='my-keys')
    op.create_index('ix_my-keys_key_value', 'my-keys', ['key_value'], unique=False)
    op.drop_column('my-keys', 'user_token')
    # ### end Alembic commands ###
