"""add user role

Revision ID: 51a17379b50f
Revises: 34a0a369c8c3
Create Date: 2022-12-31 15:54:15.485330

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '51a17379b50f'
down_revision = '34a0a369c8c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user_role = postgresql.ENUM('super_admin', 'admin', 'user',name='user_role')
    user_role.create(op.get_bind())
    op.add_column('users', sa.Column('role', sa.Enum('super_admin', 'admin', 'user', name='user_role'), nullable=False, server_default='user'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
