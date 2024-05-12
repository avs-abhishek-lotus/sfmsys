from app import db
from datetime import datetime

class StockRequirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    str_no = db.Column(db.String(255), unique=True, nullable=False)
    str_date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.Enum('1', '2', '3'), nullable=False)
    incharge = db.Column(db.String(255), nullable=False)
    req_raised_by = db.Column(db.String(255), nullable=False)
    required_for = db.Column(db.String(255), nullable=False)
    material = db.Column(db.String(255), nullable=False)
    material_quantity = db.Column(db.Integer, nullable=False)
    amount_given = db.Column(db.Numeric(10, 2), nullable=False)
    vehicle_assigned = db.Column(db.String(255), nullable=False)
    vehicle_number = db.Column(db.String(255), nullable=False)
    driver_number = db.Column(db.String(255), nullable=False)
    attachments = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'str_no': self.str_no,
            'str_date': self.str_date.isoformat() if self.str_date else None,
            'shift': self.shift,
            'incharge': self.incharge,
            'req_raised_by': self.req_raised_by,
            'required_for': self.required_for,
            'material': self.material,
            'material_quantity': self.material_quantity,
            'amount_given': float(self.amount_given),
            'vehicle_assigned': self.vehicle_assigned,
            'vehicle_number': self.vehicle_number,
            'driver_number': self.driver_number,
            'attachments': self.attachments
        }

    def __repr__(self):
        return f'<StockRequirement {self.str_no}>'

class StockOutward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    required_for = db.Column(db.String(255), nullable=False)
    sales_type = db.Column(db.String(255), nullable=False)
    invoice_number = db.Column(db.String(255), unique=True, nullable=False)
    sr_no = db.Column(db.String(255))
    issued_by = db.Column(db.String(255), nullable=False)
    party = db.Column(db.String(255), nullable=False)
    vehicle_no = db.Column(db.String(255), nullable=False)
    material = db.Column(db.String(255), nullable=False)
    rate = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    gst = db.Column(db.Numeric(10, 2), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    mod_of_payment = db.Column(db.String(255), nullable=False)
    amount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    balance = db.Column(db.Numeric(10, 2), nullable=False)
    driver_mobile = db.Column(db.String(255), nullable=False)
    owner_mobile = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'required_for': self.required_for,
            'sales_type': self.sales_type,
            'invoice_number': self.invoice_number,
            'sr_no': self.sr_no,
            'issued_by': self.issued_by,
            'party': self.party,
            'vehicle_no': self.vehicle_no,
            'material': self.material,
            'rate': float(self.rate),
            'quantity': self.quantity,
            'gst': float(self.gst),
            'total_amount': float(self.total_amount),
            'mod_of_payment': self.mod_of_payment,
            'amount_paid': float(self.amount_paid),
            'balance': float(self.balance),
            'driver_mobile': self.driver_mobile,
            'owner_mobile': self.owner_mobile
        }

    def __repr__(self):
        return f'<StockOutward {self.invoice_number}>'

class StockInward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sti_no = db.Column(db.String(255), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.Enum('1', '2', '3'), nullable=False)
    incharge = db.Column(db.String(255), nullable=False)
    referred_by = db.Column(db.String(255))
    required_for = db.Column(db.String(255), nullable=False)
    purchase_type = db.Column(db.String(255), nullable=False)
    invoice_number = db.Column(db.String(255), nullable=False)
    sr_no = db.Column(db.String(255))
    received_by = db.Column(db.String(255), nullable=False)
    purchase_party = db.Column(db.String(255), nullable=False)
    vehicle_no = db.Column(db.String(255), nullable=False)
    material = db.Column(db.String(255), nullable=False)
    rate = db.Column(db.Numeric(10, 2), nullable=False)
    mms_quantity = db.Column(db.Integer, nullable=False)
    mains_gross = db.Column(db.Numeric(10, 2), nullable=False)
    mains_tare = db.Column(db.Numeric(10, 2), nullable=False)
    mains_net_quantity = db.Column(db.Numeric(10, 2), nullable=False)
    gst = db.Column(db.Numeric(10, 2), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    mod_of_payment = db.Column(db.String(255), nullable=False)
    amount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    balance = db.Column(db.Numeric(10, 2), nullable=False)
    driver_mobile = db.Column(db.String(255), nullable=False)
    driver_name = db.Column(db.String(255))
    loading_site = db.Column(db.String(255))
    unloading_site = db.Column(db.String(255))
    trip_amount = db.Column(db.Numeric(10, 2), nullable=False)
    beta_allowance = db.Column(db.Numeric(10, 2), nullable=False)
    total_d_amount = db.Column(db.Numeric(10, 2), nullable=False)
    d_mode_of_payment = db.Column(db.String(255), nullable=False)
    d_amount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    d_balance = db.Column(db.Numeric(10, 2), nullable=False)
    owner_mobile = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'sti_no': self.sti_no,
            'date': self.date.isoformat() if self.date else None,
            'shift': self.shift,
            'incharge': self.incharge,
            'referred_by': self.referred_by,
            'required_for': self.required_for,
            'purchase_type': self.purchase_type,
            'invoice_number': self.invoice_number,
            'sr_no': self.sr_no,
            'received_by': self.received_by,
            'purchase_party': self.purchase_party,
            'vehicle_no': self.vehicle_no,
            'material': self.material,
            'rate': float(self.rate),
            'mms_quantity': self.mms_quantity,
            'mains_gross': float(self.mains_gross),
            'mains_tare': float(self.mains_tare),
            'mains_net_quantity': float(self.mains_net_quantity),
            'gst': float(self.gst),
            'total_amount': float(self.total_amount),
            'mod_of_payment': self.mod_of_payment,
            'amount_paid': float(self.amount_paid),
            'balance': float(self.balance),
            'driver_mobile': self.driver_mobile,
            'driver_name': self.driver_name,
            'loading_site': self.loading_site,
            'unloading_site': self.unloading_site,
            'trip_amount': float(self.trip_amount),
            'beta_allowance': float(self.beta_allowance),
            'total_d_amount': float(self.total_d_amount),
            'd_mode_of_payment': self.d_mode_of_payment,
            'd_amount_paid': float(self.d_amount_paid),
            'd_balance': float(self.d_balance),
            'owner_mobile': self.owner_mobile
        }

    def __repr__(self):
        return f'<StockInward {self.sti_no}>'

class PaymentInward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voucher_number = db.Column(db.String(255), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.Enum('1', '2', '3'), nullable=False)
    incharge = db.Column(db.String(255), nullable=False)
    referred_by = db.Column(db.String(255))
    sto_number = db.Column(db.String(255))
    invoice_number = db.Column(db.String(255))
    sales_type = db.Column(db.String(255), nullable=False)
    party_name = db.Column(db.String(255), nullable=False)
    gst_number = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    mode_of_payment = db.Column(db.String(255), nullable=False)
    payment_acknowledgement = db.Column(db.String(255))
    acknowledgement_number = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'voucher_number': self.voucher_number,
            'date': self.date.isoformat() if self.date else None,
            'shift': self.shift,
            'incharge': self.incharge,
            'referred_by': self.referred_by,
            'sto_number': self.sto_number,
            'invoice_number': self.invoice_number,
            'sales_type': self.sales_type,
            'party_name': self.party_name,
            'gst_number': self.gst_number,
            'amount_paid': float(self.amount_paid),
            'mode_of_payment': self.mode_of_payment,
            'payment_acknowledgement': self.payment_acknowledgement,
            'acknowledgement_number': self.acknowledgement_number
        }

    def __repr__(self):
        return f'<PaymentInward {self.voucher_number}>'
class PaymentOutward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voucher_number = db.Column(db.String(255), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    shift = db.Column(db.Enum('1', '2', '3'), nullable=False)
    incharge = db.Column(db.String(255), nullable=False)
    referred_by = db.Column(db.String(255))
    sti_number = db.Column(db.String(255))
    invoice_number = db.Column(db.String(255))
    sales_type = db.Column(db.String(255), nullable=False)
    party_name = db.Column(db.String(255), nullable=False)
    gst_number = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    mode_of_payment = db.Column(db.String(255), nullable=False)
    payment_acknowledgement = db.Column(db.String(255))
    acknowledgement_number = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'voucher_number': self.voucher_number,
            'date': self.date.isoformat() if self.date else None,
            'shift': self.shift,
            'incharge': self.incharge,
            'referred_by': self.referred_by,
            'sti_number': self.sti_number,
            'invoice_number': self.invoice_number,
            'sales_type': self.sales_type,
            'party_name': self.party_name,
            'gst_number': self.gst_number,
            'amount_paid': float(self.amount_paid),
            'mode_of_payment': self.mode_of_payment,
            'payment_acknowledgement': self.payment_acknowledgement,
            'acknowledgement_number': self.acknowledgement_number
        }

    def __repr__(self):
        return f'<PaymentOutward {self.voucher_number}>'