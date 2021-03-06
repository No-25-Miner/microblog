"""new version

Revision ID: 88772727c146
Revises: 
Create Date: 2022-02-24 10:31:41.709174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88772727c146'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Posts',
    sa.Column('rec_id', sa.Integer(), nullable=False),
    sa.Column('anther_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('rec_id')
    )
    op.create_index(op.f('ix_Posts_anther_id'), 'Posts', ['anther_id'], unique=False)
    op.create_table('followers',
    sa.Column('rec_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('rec_id')
    )
    op.create_index(op.f('ix_followers_followed_id'), 'followers', ['followed_id'], unique=False)
    op.create_index(op.f('ix_followers_follower_id'), 'followers', ['follower_id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_followers_follower_id'), table_name='followers')
    op.drop_index(op.f('ix_followers_followed_id'), table_name='followers')
    op.drop_table('followers')
    op.drop_index(op.f('ix_Posts_anther_id'), table_name='Posts')
    op.drop_table('Posts')
    # ### end Alembic commands ###
