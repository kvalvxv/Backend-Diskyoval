"""Add image_url and image_public_id columns

Revision ID: e57cba1d89ad
Revises: 760194d395da
Create Date: 2026-02-18 16:45:34.534142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e57cba1d89ad'
down_revision = '760194d395da'
branch_labels = None
depends_on = None


def upgrade():
    # Add image columns to products table
    op.add_column('products', sa.Column('image_url', sa.String(500), nullable=True))
    op.add_column('products', sa.Column('image_public_id', sa.String(255), nullable=True))


def downgrade():
    # Remove image columns from products table
    op.drop_column('products', 'image_public_id')
    op.drop_column('products', 'image_url')
