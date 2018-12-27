"""Add imports column to yara rules

Revision ID: b67c53c89680
Revises: 0896164f6037
Create Date: 2018-05-27 16:33:43.266789

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b67c53c89680'
down_revision = '0896164f6037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('yara_rules', sa.Column('imports', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('yara_rules', 'imports')
    # ### end Alembic commands ###
