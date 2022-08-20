"""empty message

Revision ID: 1f3ba0e27946
Revises: a0c935fc53d6
Create Date: 2022-08-11 11:42:56.221342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f3ba0e27946'
down_revision = 'a0c935fc53d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Venue2')
    
    op.add_column('Artist', sa.Column('website_link', sa.String(), nullable=False))
    op.add_column('Artist', sa.Column('seeking_venue', sa.String(), nullable=False))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=False))
    op.add_column('Venue', sa.Column('genres', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(), nullable=True))
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Venue', 'facebook_link',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'facebook_link',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'website_link')
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'website_link')
   
    op.create_table('Venue2',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Venue2_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('facebook_link', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Venue2_pkey')
    )
    # ### end Alembic commands ###
