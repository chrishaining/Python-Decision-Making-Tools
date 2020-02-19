"""empty message

Revision ID: 222c16aa02fb
Revises: 9bf5b25f498a
Create Date: 2020-02-19 22:10:20.913680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '222c16aa02fb'
down_revision = '9bf5b25f498a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cohort', 'cohort_name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.create_foreign_key(None, 'student', 'cohort', ['cohort_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.alter_column('cohort', 'cohort_name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###
