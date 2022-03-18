"""empty message

Revision ID: c43bbd247806
Revises: 33d5993a1918
Create Date: 2022-03-18 22:08:56.983118

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c43bbd247806'
down_revision = '33d5993a1918'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('Favorites_List',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('USER_ID', sa.Integer(), nullable=True),
    # sa.Column('FAV_CHARACTER', sa.Integer(), nullable=True),
    # sa.Column('FAV_PLANET', sa.Integer(), nullable=True),
    # sa.ForeignKeyConstraint(['FAV_CHARACTER'], ['Character.id'], ),
    # sa.ForeignKeyConstraint(['FAV_PLANET'], ['Planet.id'], ),
    # sa.ForeignKeyConstraint(['USER_ID'], ['Userr.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('Planet',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('PLANET_NAME', sa.String(length=250), nullable=True),
    # sa.Column('PLANET_ROT_PERIOD', sa.Integer(), nullable=True),
    # sa.Column('PLANET_TRANS_PERIOD', sa.Integer(), nullable=True),
    # sa.Column('PLANET_DIAMETER', sa.Integer(), nullable=True),
    # sa.Column('PLANET_CLIMATE', sa.String(length=250), nullable=True),
    # sa.Column('PLANET_GRAVITY', sa.String(length=250), nullable=True),
    # sa.Column('PLANET_TERRAIN', sa.String(length=250), nullable=True),
    # sa.Column('PLANET_SURFACE_WATER', sa.Integer(), nullable=True),
    # sa.Column('PLANET_POP', sa.Integer(), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('Userr',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('USER_FNAME', sa.String(length=250), nullable=False),
    # sa.Column('USER_LNAME', sa.String(length=250), nullable=False),
    # sa.Column('USER_EMAIL', sa.String(length=250), nullable=False),
    # sa.Column('USER_PASSWORD', sa.String(length=250), nullable=False),
    # sa.Column('USER_FAVORITE_LIST', sa.Integer(), nullable=True),
    # sa.ForeignKeyConstraint(['USER_FAVORITE_LIST'], ['Favorites_List.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('Character',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('CHAR_SPECIES', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_NAME', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_GENDER', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_YOB', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_HEIGHT', sa.Integer(), nullable=True),
    # sa.Column('CHAR_WEIGHT', sa.Integer(), nullable=True),
    # sa.Column('CHAR_EYE_COLOR', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_HAIR_COLOR', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_SKIN_COLOR', sa.String(length=250), nullable=True),
    # sa.Column('CHAR_HOMEWORLD', sa.Integer(), nullable=True),
    # sa.ForeignKeyConstraint(['CHAR_HOMEWORLD'], ['Planet.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.alter_column('user', 'is_active',
    #            existing_type=mysql.TINYINT(display_width=1),
    #            nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.drop_table('Character')
    op.drop_table('Userr')
    op.drop_table('Planet')
    op.drop_table('Favorites_List')
    # ### end Alembic commands ###
