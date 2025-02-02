"""empty message

Revision ID: 2aa1acb64587
Revises: b45c072f1eae
Create Date: 2023-10-11 01:50:02.971667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aa1acb64587'
down_revision = 'b45c072f1eae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('diameter', sa.String(length=30), nullable=True),
    sa.Column('rotation_period', sa.String(length=30), nullable=False),
    sa.Column('orbital_period', sa.String(length=30), nullable=True),
    sa.Column('gravity', sa.Float(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=30), nullable=True),
    sa.Column('terrain', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('gravity'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('orbital_period'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('terrain')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
