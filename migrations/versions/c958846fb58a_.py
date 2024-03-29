"""empty message

Revision ID: c958846fb58a
Revises: 
Create Date: 2024-03-17 22:02:26.408718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c958846fb58a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('num_bedrooms', sa.Integer(), nullable=True),
    sa.Column('num_bathrooms', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=40), nullable=True),
    sa.Column('property_type', sa.String(length=20), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
