"""empty message

Revision ID: 067b65f83761
Revises: 
Create Date: 2023-05-05 22:12:18.757486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067b65f83761'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('task', sa.String(length=100), nullable=False),
    sa.Column('summary', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_list')
    # ### end Alembic commands ###
