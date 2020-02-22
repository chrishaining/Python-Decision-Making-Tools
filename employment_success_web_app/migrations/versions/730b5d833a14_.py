"""empty message

Revision ID: 730b5d833a14
Revises: a67fc6b510af
Create Date: 2020-02-22 14:52:38.163304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '730b5d833a14'
down_revision = 'a67fc6b510af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_one', sa.Text(), nullable=True),
    sa.Column('cohort_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cohort_id'], ['cohort.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_survey_question_one'), 'survey', ['question_one'], unique=False)
    op.create_foreign_key(None, 'student', 'cohort', ['cohort_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_index(op.f('ix_survey_question_one'), table_name='survey')
    op.drop_table('survey')
    # ### end Alembic commands ###
