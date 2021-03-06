"""empty message

Revision ID: 4fff0e7fd207
Revises: 
Create Date: 2022-03-25 15:38:20.630697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fff0e7fd207'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('CHAR_NAME', sa.String(length=250), nullable=True),
    sa.Column('CHAR_SPECIES', sa.String(length=250), nullable=True),
    sa.Column('CHAR_GENDER', sa.String(length=250), nullable=True),
    sa.Column('CHAR_YOB', sa.String(length=250), nullable=True),
    sa.Column('CHAR_HEIGHT', sa.Integer(), nullable=True),
    sa.Column('CHAR_WEIGHT', sa.Integer(), nullable=True),
    sa.Column('CHAR_EYE_COLOR', sa.String(length=250), nullable=True),
    sa.Column('CHAR_HAIR_COLOR', sa.String(length=250), nullable=True),
    sa.Column('CHAR_SKIN_COLOR', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('PLANET_NAME', sa.String(length=250), nullable=True),
    sa.Column('PLANET_ROT_PERIOD', sa.Integer(), nullable=True),
    sa.Column('PLANET_TRANS_PERIOD', sa.Integer(), nullable=True),
    sa.Column('PLANET_DIAMETER', sa.Integer(), nullable=True),
    sa.Column('PLANET_CLIMATE', sa.String(length=250), nullable=True),
    sa.Column('PLANET_GRAVITY', sa.String(length=250), nullable=True),
    sa.Column('PLANET_TERRAIN', sa.String(length=250), nullable=True),
    sa.Column('PLANET_SURFACE_WATER', sa.Integer(), nullable=True),
    sa.Column('PLANET_POP', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('USER_FNAME', sa.String(length=250), nullable=False),
    sa.Column('USER_LNAME', sa.String(length=250), nullable=False),
    sa.Column('USER_EMAIL', sa.String(length=250), nullable=False),
    sa.Column('USER_PASSWORD', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Favorites_List',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('USER_ID', sa.Integer(), nullable=True),
    sa.Column('FAV_CHARACTER_ID', sa.Integer(), nullable=True),
    sa.Column('FAV_PLANET_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['FAV_CHARACTER_ID'], ['Character.id'], ),
    sa.ForeignKeyConstraint(['FAV_PLANET_ID'], ['Planet.id'], ),
    sa.ForeignKeyConstraint(['USER_ID'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Favorites_List')
    op.drop_table('User')
    op.drop_table('Planet')
    op.drop_table('Character')
    # ### end Alembic commands ###
