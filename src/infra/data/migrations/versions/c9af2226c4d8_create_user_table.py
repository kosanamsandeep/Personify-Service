"""create user table

Revision ID: c9af2226c4d8
Revises: 
Create Date: 2023-06-05 11:08:41.283912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9af2226c4d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('username', sa.String(
                        length=100), nullable=False),
                    sa.Column('password', sa.String(
                        length=100), nullable=False),
                    sa.Column('full_name', sa.String(
                        length=100), nullable=False),
                    sa.Column('date_of_birth', sa.Date(), nullable=False),
                    sa.Column('email', sa.String(length=100), nullable=True),
                    sa.Column('_id', sa.UUID(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('_id'),
                    sa.UniqueConstraint('username')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
