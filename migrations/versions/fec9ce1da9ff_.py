"""회원가입이 됩니다! -juice500

Revision ID: fec9ce1da9ff
Revises: 1561a57ed187
Create Date: 2016-02-20 12:19:17.890009

"""

# revision identifiers, used by Alembic.
revision = 'fec9ce1da9ff'
down_revision = '1561a57ed187'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=60), nullable=False),
    sa.Column('first_name_kr', sa.String(length=50), nullable=False),
    sa.Column('last_name_kr', sa.String(length=50), nullable=False),
    sa.Column('first_name_en', sa.String(length=50), nullable=False),
    sa.Column('middle_name_en', sa.String(length=50), nullable=True),
    sa.Column('last_name_en', sa.String(length=50), nullable=False),
    sa.Column('student_number', sa.Integer(), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###