"""empty message

Revision ID: df6643750333
Revises: 
Create Date: 2021-09-22 22:26:28.256288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df6643750333'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=30), nullable=False),
    sa.Column('lastname', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=30), nullable=True),
    sa.Column('favorite_name', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('birth_year', sa.String(length=30), nullable=True),
    sa.Column('gender', sa.String(length=30), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorites.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=30), nullable=True),
    sa.Column('terrain', sa.String(length=30), nullable=True),
    sa.Column('population', sa.String(length=30), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorites.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=True),
    sa.Column('manufacturer', sa.String(length=50), nullable=True),
    sa.Column('passengers', sa.String(length=30), nullable=True),
    sa.Column('vehicle_class', sa.String(length=50), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorites.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    op.drop_table('favorites')
    op.drop_table('user')
    # ### end Alembic commands ###
