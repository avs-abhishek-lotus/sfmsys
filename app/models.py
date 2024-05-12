from app import db

class StockRequirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    str_no = db.Column(db.String(255))
    str_date = db.Column(db.Date)
    shift = db.Column(db.Enum('1', '2', '3'))
    incharge = db.Column(db.String(255))
    req_raised_by = db.Column(db.String(255))
    required_for = db.Column(db.String(255))
    material = db.Column(db.String(255))
    material_quantity = db.Column(db.Integer)
    amount_given = db.Column(db.Numeric(10, 2))
    vehicle_assigned = db.Column(db.String(255))
    vehicle_number = db.Column(db.String(255))
    driver_number = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'str_no': self.str_no,
            # Add other fields
        }

    def __repr__(self):
        return f'<StockRequirement {self.str_no}>'

class StockOutward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    required_for = db.Column(db.String(255))
    sales_type = db.Column(db.String(255))
    invoice_number = db.Column(db.String(255))
    sr_no = db.Column(db.String(255))
    issued_by = db.Column(db.String(255))
    party = db.Column(db.String(255))
    vehicle_no = db.Column(db.String(255))
    material = db.Column(db.String(255))
    rate = db.Column(db.Numeric(10, 2))
    quantity = db.Column(db.Integer)
    gst = db.Column(db.Numeric(10, 2))
    total_amount = db.Column(db.Numeric(10, 2))
    mod_of_payment = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric(10, 2))
    balance = db.Column(db.Numeric(10, 2))
    driver_mobile = db.Column(db.String(255))
    owner_mobile = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'required_for': self.required_for,
            # Add other fields
        }

    def __repr__(self):
        return f'<StockOutward {self.invoice_number}>'

class StockInward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sti_no = db.Column(db.String(255))
    date = db.Column(db.Date)
    shift = db.Column(db.Enum('1', '2', '3'))
    incharge = db.Column(db.String(255))
    referred_by = db.Column(db.String(255))
    required_for = db.Column(db.String(255))
    purchase_type = db.Column(db.String(255))
    invoice_number = db.Column(db.String(255))
    sr_no = db.Column(db.String(255))
    received_by = db.Column(db.String(255))
    purchase_party = db.Column(db.String(255))
    vehicle_no = db.Column(db.String(255))
    material = db.Column(db.String(255))
    rate = db.Column(db.Numeric(10, 2))
    mms_quantity = db.Column(db.Integer)
    mains_gross = db.Column(db.Numeric(10, 2))
    mains_tare = db.Column(db.Numeric(10, 2))
    mains_net_quantity = db.Column(db.Numeric(10, 2))
    gst = db.Column(db.Numeric(10, 2))
    total_amount = db.Column(db.Numeric(10, 2))
    mod_of_payment = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric(10, 2))
    balance = db.Column(db.Numeric(10, 2))
    driver_mobile = db.Column(db.String(255))
    driver_name = db.Column(db.String(255))
    loading_site = db.Column(db.String(255))
    unloading_site = db.Column(db.String(255))
    trip_amount = db.Column(db.Numeric(10, 2))
    beta_allowance = db.Column(db.Numeric(10, 2))
    total_d_amount = db.Column(db.Numeric(10, 2))
    d_mode_of_payment = db.Column(db.String(255))
    d_amount_paid = db.Column(db.Numeric(10, 2))
    d_balance = db.Column(db.Numeric(10, 2))
    owner_mobile = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'sti_no': self.sti_no,
            # Add other fields
        }

    def __repr__(self):
        return f'<StockInward {self.sti_no}>'

class PaymentInward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voucher_number = db.Column(db.String(255))
    date = db.Column(db.Date)
    shift = db.Column(db.Enum('1', '2', '3'))
    incharge = db.Column(db.String(255))
    referred_by = db.Column(db.String(255))
    sto_number = db.Column(db.String(255))
    invoice_number = db.Column(db.String(255))
    sales_type = db.Column(db.String(255))
    party_name = db.Column(db.String(255))
    gst_number = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric(10, 2))
    mode_of_payment = db.Column(db.String(255))
    payment_acknowledgement = db.Column(db.String(255))
    acknowledgement_number = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'voucher_number': self.voucher_number,
            # Continue adding other fields
        }

class PaymentOutward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voucher_number = db.Column(db.String(255))
    date = db.Column(db.Date)
    shift = db.Column(db.Enum('1', '2', '3'))
    incharge = db.Column(db.String(255))
    referred_by = db.Column(db.String(255))
    sti_number = db.Column(db.String(255))
    invoice_number = db.Column(db.String(255))
    sales_type = db.Column(db.String(255))
    party_name = db.Column(db.String(255))
    gst_number = db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric(10, 2))
    mode_of_payment = db.Column(db.String(255))
    payment_acknowledgement = db.Column(db.String(255))
    acknowledgement_number = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'voucher_number': self.voucher_number,
            # Continue adding other fields
        }
