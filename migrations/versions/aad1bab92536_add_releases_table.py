"""Add releases table

Revision ID: aad1bab92536
Revises: 0bd5407cc66d
Create Date: 2017-08-29 15:20:45.220826

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'aad1bab92536'
down_revision = '0bd5407cc66d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('releases',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=500), nullable=False),
                    sa.Column('is_test_release', sa.Integer(), nullable=True),
                    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('release_data', sa.Text(), nullable=False),
                    sa.Column('created_user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['created_user_id'], ['kb_users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('releases')
    # ### end Alembic commands ###
