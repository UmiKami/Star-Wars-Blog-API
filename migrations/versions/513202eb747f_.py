"""empty message

Revision ID: 513202eb747f
Revises: 91536577c80e
Create Date: 2022-03-28 16:53:30.699352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513202eb747f'
down_revision = '91536577c80e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Favorites_List', sa.Column('USER_ID', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Favorites_List', 'User', ['USER_ID'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Favorites_List', type_='foreignkey')
    op.drop_column('Favorites_List', 'USER_ID')
    # ### end Alembic commands ###
