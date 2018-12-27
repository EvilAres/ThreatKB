"""initial migration

Revision ID: 2221286081e8
Revises:
Create Date: 2017-08-06 17:05:25.523671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2221286081e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cfg_states',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('state', sa.String(length=32), nullable=True),
                    sa.Column('is_release_state', sa.Integer(), nullable=True),
                    sa.Column('is_retired_state', sa.Integer(), nullable=True),
                    sa.Column('is_staging_state', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('tags_mapping',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('source_table', sa.Enum('c2dns', 'c2ip', 'yara_rule', 'tasks'), nullable=True),
                    sa.Column('source_id', sa.Integer(), nullable=True),
                    sa.Column('tag_id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(u'ix_tags_mapping_source_id', 'tags_mapping', ['source_id'], unique=False)
    op.create_index(u'ix_tags_mapping_source_table', 'tags_mapping', ['source_table'], unique=False)
    op.create_index(u'ix_tags_mapping_tag_id', 'tags_mapping', ['tag_id'], unique=False)
    op.create_table('cfg_reference_text_templates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('template_text', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kb_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('c2ip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ip', sa.String(length=15), nullable=True),
    sa.Column('asn', sa.String(length=128), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('st', sa.String(length=32), nullable=True),
    sa.Column('state', sa.String(length=32), nullable=True),
    sa.Column('reference_link', sa.String(length=2048), nullable=True),
    sa.Column('reference_text', sa.String(length=2048), nullable=True),
    sa.Column('expiration_type', sa.String(length=32), nullable=True),
    sa.Column('expiration_timestamp', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=False),
    sa.Column('modified_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_user_id'], ['kb_users.id'], ),
    sa.ForeignKeyConstraint(['modified_user_id'], ['kb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_c2ip_ip', 'c2ip', ['ip'], unique=False)
    op.create_index(u'ix_c2ip_state', 'c2ip', ['state'], unique=False)
    op.create_table('c2dns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('state', sa.String(length=32), nullable=True),
    sa.Column('domain_name', sa.String(length=255), nullable=True),
    sa.Column('match_type', sa.Enum('exact', 'wildcard'), nullable=True),
    sa.Column('reference_link', sa.String(length=2048), nullable=True),
    sa.Column('reference_text', sa.String(length=2048), nullable=True),
    sa.Column('expiration_type', sa.String(length=32), nullable=True),
    sa.Column('expiration_timestamp', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=False),
    sa.Column('modified_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_user_id'], ['kb_users.id'], ),
    sa.ForeignKeyConstraint(['modified_user_id'], ['kb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_c2dns_domain_name', 'c2dns', ['domain_name'], unique=False)
    op.create_index(u'ix_c2dns_state', 'c2dns', ['state'], unique=False)
    op.create_table('yara_rules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('state', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('test_status', sa.String(length=16), nullable=True),
    sa.Column('confidence', sa.Integer(), nullable=True),
    sa.Column('severity', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=4096), nullable=True),
    sa.Column('category', sa.String(length=32), nullable=True),
    sa.Column('file_type', sa.String(length=32), nullable=True),
    sa.Column('subcategory1', sa.String(length=32), nullable=True),
    sa.Column('subcategory2', sa.String(length=32), nullable=True),
    sa.Column('subcategory3', sa.String(length=32), nullable=True),
    sa.Column('reference_link', sa.String(length=2048), nullable=True),
    sa.Column('reference_text', sa.String(length=2048), nullable=True),
    sa.Column('condition', sa.String(length=2048), nullable=True),
    sa.Column('strings', sa.String(length=30000), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=False),
    sa.Column('modified_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_user_id'], ['kb_users.id'], ),
    sa.ForeignKeyConstraint(['modified_user_id'], ['kb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_yara_rules_name', 'yara_rules', ['name'], unique=False)
    op.create_index(u'ix_yara_rules_state', 'yara_rules', ['state'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('comment', sa.String(length=65000), nullable=True),
    sa.Column('entity_type', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['kb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_comments_entity_id', 'comments', ['entity_id'], unique=False)
    op.create_index(u'ix_comments_entity_type', 'comments', ['entity_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_comments_entity_type', table_name='comments')
    op.drop_index(u'ix_comments_entity_id', table_name='comments')
    op.drop_table('comments')
    op.drop_index(u'ix_yara_rules_state', table_name='yara_rules')
    op.drop_index(u'ix_yara_rules_name', table_name='yara_rules')
    op.drop_table('yara_rules')
    op.drop_index(u'ix_c2dns_state', table_name='c2dns')
    op.drop_index(u'ix_c2dns_domain_name', table_name='c2dns')
    op.drop_table('c2dns')
    op.drop_index(u'ix_c2ip_state', table_name='c2ip')
    op.drop_index(u'ix_c2ip_ip', table_name='c2ip')
    op.drop_table('c2ip')
    op.drop_table('kb_users')
    op.drop_table('cfg_reference_text_templates')
    op.drop_index(u'ix_tags_mapping_tag_id', table_name='tags_mapping')
    op.drop_index(u'ix_tags_mapping_source_table', table_name='tags_mapping')
    op.drop_index(u'ix_tags_mapping_source_id', table_name='tags_mapping')
    op.drop_table('tags_mapping')
    op.drop_table('cfg_states')
    op.drop_table('tags')
    # ### end Alembic commands ###
