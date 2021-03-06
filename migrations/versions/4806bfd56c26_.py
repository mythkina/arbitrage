"""empty message

Revision ID: 4806bfd56c26
Revises: 8a6cf65d3952
Create Date: 2020-03-28 19:30:45.510592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4806bfd56c26'
down_revision = '8a6cf65d3952'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('indice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('stockId', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('areaCode', sa.String(length=20), nullable=True),
    sa.Column('stockType', sa.String(length=20), nullable=True),
    sa.Column('exchange', sa.String(length=20), nullable=True),
    sa.Column('stockCode', sa.String(length=20), nullable=True),
    sa.Column('launchDate', sa.Date(), nullable=True),
    sa.Column('currency', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pe_ttm', sa.Column('exchange', sa.String(length=10), nullable=True))
    op.add_column('pe_ttm', sa.Column('name', sa.String(length=20), nullable=True))
    op.add_column('pe_ttm', sa.Column('type', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pe_ttm', 'type')
    op.drop_column('pe_ttm', 'name')
    op.drop_column('pe_ttm', 'exchange')
    op.drop_table('indice')
    # ### end Alembic commands ###
