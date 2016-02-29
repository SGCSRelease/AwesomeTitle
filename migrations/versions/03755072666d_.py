"""Nickname DB를 추가하고 NickRecom DB의 변수명을 바꿨습니다.  -jmg
		fromA -> recommender, toB -> username
		alter_column()의 사용법을 알았습니다!

Revision ID: 03755072666d
Revises: dbdb246795ee
Create Date: 2016-02-25 17:42:15.977272

"""

# revision identifiers, used by Alembic.
revision = '03755072666d'
down_revision = 'dbdb246795ee'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nickname',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('nick', sa.String(length=50), nullable=True),
    sa.Column('recommender', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('idx')
    )
    #op.add_column('nickrecom', sa.Column('recommender', sa.String(length=50), nullable=True))
    #op.add_column('nickrecom', sa.Column('username', sa.String(length=50), nullable=True))
    #op.drop_column('nickrecom', 'toB')
    #op.drop_column('nickrecom', 'fromA')
    op.alter_column('nickrecom', 'fromA', new_column_name='recommender', existing_type=mysql.VARCHAR(length=50), existing_server_default="", existing_nullable=True)
    op.alter_column('nickrecom', 'toB', new_column_name='username', existing_type=mysql.VARCHAR(length=50), existing_server_default="", existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('nickrecom', sa.Column('fromA', mysql.VARCHAR(length=50), nullable=True))
    #op.add_column('nickrecom', sa.Column('toB', mysql.VARCHAR(length=50), nullable=True))
    #op.drop_column('nickrecom', 'username')
    #op.drop_column('nickrecom', 'recommender')
    op.alter_column('nickrecom', 'recommender', new_column_name='fromA', existing_type=mysql.VARCHAR(length=50), existing_server_default="", existing_nullable=True)
    op.alter_column('nickrecom', 'username', new_column_name='toB', existing_type=mysql.VARCHAR(length=50), existing_server_default="", existing_nullable=True)
    op.drop_table('nickname')
    ### end Alembic commands ###