"""Activity Log

Revision ID: 8c3bbaef0f9c
Revises: b52a9e4d9587
Create Date: 2018-12-26 23:16:46.952688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8c3bbaef0f9c'
down_revision = 'b52a9e4d9587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_type', sa.String(length=256), nullable=True),
    sa.Column('activity_text', sa.String(length=65000), nullable=True),
    sa.Column('activity_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('entity_type', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['kb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_activity_log_entity_id', 'activity_log', ['entity_id'], unique=False)
    op.create_index(u'ix_activity_log_entity_type', 'activity_log', ['entity_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_activity_log_entity_type', table_name='activity_log')
    op.drop_index(u'ix_activity_log_entity_id', table_name='activity_log')
    op.drop_table('activity_log')
    # ### end Alembic commands ###