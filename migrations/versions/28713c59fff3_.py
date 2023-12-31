"""empty message

Revision ID: 28713c59fff3
Revises: 
Create Date: 2023-08-16 10:29:54.950644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28713c59fff3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('glossary',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('translation', sa.String(length=200), nullable=False),
    sa.Column('pattern', sa.String(length=200), nullable=False),
    sa.Column('grammar_info', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('word_id')
    )
    op.create_table('programs_of_study',
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('institution', sa.String(length=200), nullable=False),
    sa.Column('program_name', sa.String(length=200), nullable=False),
    sa.Column('degrees', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('specialities', sa.String(length=150), nullable=False),
    sa.Column('program_url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('program_id')
    )
    op.create_table('saga_locations',
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('location_name', sa.String(length=200), nullable=False),
    sa.Column('latitude', sa.Float(precision=50), nullable=False),
    sa.Column('longitude', sa.Float(precision=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('location_id')
    )
    op.create_table('societies',
    sa.Column('affiliation_id', sa.Integer(), nullable=False),
    sa.Column('society_name', sa.String(length=200), nullable=False),
    sa.Column('focus', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('society_url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('affiliation_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('collection',
    sa.Column('collection_id', sa.Integer(), nullable=False),
    sa.Column('book_title', sa.String(length=200), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('year_published', sa.String(length=20), nullable=False),
    sa.Column('language', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('collection_id')
    )
    op.create_table('conference',
    sa.Column('conference_id', sa.Integer(), nullable=False),
    sa.Column('conference_title', sa.String(length=200), nullable=False),
    sa.Column('focus', sa.String(length=200), nullable=False),
    sa.Column('conference_url', sa.String(length=200), nullable=False),
    sa.Column('affiliation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['affiliation_id'], ['societies.affiliation_id'], ),
    sa.PrimaryKeyConstraint('conference_id')
    )
    op.create_table('journal',
    sa.Column('journal_id', sa.Integer(), nullable=False),
    sa.Column('journal_title', sa.String(length=200), nullable=False),
    sa.Column('focus', sa.String(length=200), nullable=True),
    sa.Column('language', sa.String(length=20), nullable=False),
    sa.Column('journal_url', sa.String(length=200), nullable=False),
    sa.Column('affiliation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['affiliation_id'], ['societies.affiliation_id'], ),
    sa.PrimaryKeyConstraint('journal_id')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('journal')
    op.drop_table('conference')
    op.drop_table('collection')
    op.drop_table('user')
    op.drop_table('societies')
    op.drop_table('saga_locations')
    op.drop_table('programs_of_study')
    op.drop_table('glossary')
    # ### end Alembic commands ###
