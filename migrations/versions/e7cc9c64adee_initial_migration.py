"""Initial migration

Revision ID: e7cc9c64adee
Revises: 
Create Date: 2024-05-13 16:52:09.936281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7cc9c64adee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_inward',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voucher_number', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('shift', sa.Enum('1', '2', '3'), nullable=False),
    sa.Column('incharge', sa.String(length=255), nullable=False),
    sa.Column('referred_by', sa.String(length=255), nullable=True),
    sa.Column('sto_number', sa.String(length=255), nullable=True),
    sa.Column('invoice_number', sa.String(length=255), nullable=True),
    sa.Column('sales_type', sa.String(length=255), nullable=False),
    sa.Column('party_name', sa.String(length=255), nullable=False),
    sa.Column('gst_number', sa.String(length=255), nullable=True),
    sa.Column('amount_paid', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mode_of_payment', sa.String(length=255), nullable=False),
    sa.Column('payment_acknowledgement', sa.String(length=255), nullable=True),
    sa.Column('acknowledgement_number', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('voucher_number')
    )
    op.create_table('payment_outward',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voucher_number', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('shift', sa.Enum('1', '2', '3'), nullable=False),
    sa.Column('incharge', sa.String(length=255), nullable=False),
    sa.Column('referred_by', sa.String(length=255), nullable=True),
    sa.Column('sti_number', sa.String(length=255), nullable=True),
    sa.Column('invoice_number', sa.String(length=255), nullable=True),
    sa.Column('sales_type', sa.String(length=255), nullable=False),
    sa.Column('party_name', sa.String(length=255), nullable=False),
    sa.Column('gst_number', sa.String(length=255), nullable=True),
    sa.Column('amount_paid', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mode_of_payment', sa.String(length=255), nullable=False),
    sa.Column('payment_acknowledgement', sa.String(length=255), nullable=True),
    sa.Column('acknowledgement_number', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('voucher_number')
    )
    op.create_table('stock_inward',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sti_no', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('shift', sa.Enum('1', '2', '3'), nullable=False),
    sa.Column('incharge', sa.String(length=255), nullable=False),
    sa.Column('referred_by', sa.String(length=255), nullable=True),
    sa.Column('required_for', sa.String(length=255), nullable=False),
    sa.Column('purchase_type', sa.String(length=255), nullable=False),
    sa.Column('invoice_number', sa.String(length=255), nullable=False),
    sa.Column('sr_no', sa.String(length=255), nullable=True),
    sa.Column('received_by', sa.String(length=255), nullable=False),
    sa.Column('purchase_party', sa.String(length=255), nullable=False),
    sa.Column('vehicle_no', sa.String(length=255), nullable=False),
    sa.Column('material', sa.String(length=255), nullable=False),
    sa.Column('rate', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mms_quantity', sa.Integer(), nullable=False),
    sa.Column('mains_gross', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mains_tare', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mains_net_quantity', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('gst', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mod_of_payment', sa.String(length=255), nullable=False),
    sa.Column('amount_paid', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('driver_mobile', sa.String(length=255), nullable=False),
    sa.Column('driver_name', sa.String(length=255), nullable=True),
    sa.Column('loading_site', sa.String(length=255), nullable=True),
    sa.Column('unloading_site', sa.String(length=255), nullable=True),
    sa.Column('trip_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('beta_allowance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('total_d_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('d_mode_of_payment', sa.String(length=255), nullable=False),
    sa.Column('d_amount_paid', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('d_balance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('owner_mobile', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sti_no')
    )
    op.create_table('stock_outward',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('required_for', sa.String(length=255), nullable=False),
    sa.Column('sales_type', sa.String(length=255), nullable=False),
    sa.Column('invoice_number', sa.String(length=255), nullable=False),
    sa.Column('sr_no', sa.String(length=255), nullable=True),
    sa.Column('issued_by', sa.String(length=255), nullable=False),
    sa.Column('party', sa.String(length=255), nullable=False),
    sa.Column('vehicle_no', sa.String(length=255), nullable=False),
    sa.Column('material', sa.String(length=255), nullable=False),
    sa.Column('rate', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('gst', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('mod_of_payment', sa.String(length=255), nullable=False),
    sa.Column('amount_paid', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('driver_mobile', sa.String(length=255), nullable=False),
    sa.Column('owner_mobile', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('invoice_number')
    )
    op.create_table('stock_requirement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('str_no', sa.String(length=255), nullable=False),
    sa.Column('str_date', sa.Date(), nullable=False),
    sa.Column('shift', sa.Enum('1', '2', '3'), nullable=False),
    sa.Column('incharge', sa.String(length=255), nullable=False),
    sa.Column('req_raised_by', sa.String(length=255), nullable=False),
    sa.Column('required_for', sa.String(length=255), nullable=False),
    sa.Column('material', sa.String(length=255), nullable=False),
    sa.Column('material_quantity', sa.Integer(), nullable=False),
    sa.Column('amount_given', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('vehicle_assigned', sa.String(length=255), nullable=False),
    sa.Column('vehicle_number', sa.String(length=255), nullable=False),
    sa.Column('driver_number', sa.String(length=255), nullable=False),
    sa.Column('attachments', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('str_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_requirement')
    op.drop_table('stock_outward')
    op.drop_table('stock_inward')
    op.drop_table('payment_outward')
    op.drop_table('payment_inward')
    # ### end Alembic commands ###