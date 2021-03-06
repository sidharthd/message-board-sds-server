"""empty message

Revision ID: 204e70e6024d
Revises: 
Create Date: 2018-01-18 10:56:28.333098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '204e70e6024d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tweet', sa.String(length=140), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=140), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tweet_id'], ['tweet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('tweet')
    # ### end Alembic commands ###
