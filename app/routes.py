from flask import request, jsonify
from app import app, db
from app.models import StockRequirement, StockOutward, StockInward
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/')
def index():
    return "Welcome to the Inventory Management System!"

@app.route('/add_str', methods=['POST'])
def add_str():
    if request.method == 'POST':
        data = request.json
        new_str = StockRequirement(
            str_no=data.get('str_no'),
            str_date=data.get('str_date'),
            shift=data.get('shift'),
            incharge=data.get('incharge'),
            req_raised_by=data.get('req_raised_by'),
            required_for=data.get('required_for'),
            material=data.get('material'),
            material_quantity=data.get('material_quantity'),
            amount_given=data.get('amount_given'),
            vehicle_assigned=data.get('vehicle_assigned'),
            vehicle_number=data.get('vehicle_number'),
            driver_number=data.get('driver_number')
        )
        db.session.add(new_str)
        db.session.commit()
        return jsonify({'message': 'Stock Requirement added successfully'}), 201

@app.route('/get_strs', methods=['GET'])
def get_strs():
    all_strs = StockRequirement.query.all()
    return jsonify([str.to_dict() for str in all_strs]), 200

# Add Stock Outward
@app.route('/add_sto', methods=['POST'])
def add_sto():
    data = request.json
    new_sto = StockOutward(
        required_for=data.get('required_for'),
        sales_type=data.get('sales_type'),
        invoice_number=data.get('invoice_number'),
        sr_no=data.get('sr_no'),
        issued_by=data.get('issued_by'),
        party=data.get('party'),
        vehicle_no=data.get('vehicle_no'),
        material=data.get('material'),
        rate=data.get('rate'),
        quantity=data.get('quantity'),
        gst=data.get('gst'),
        total_amount=data.get('total_amount'),
        mod_of_payment=data.get('mod_of_payment'),
        amount_paid=data.get('amount_paid'),
        balance=data.get('balance'),
        driver_mobile=data.get('driver_mobile'),
        owner_mobile=data.get('owner_mobile')
    )
    db.session.add(new_sto)
    db.session.commit()
    return jsonify({'message': 'Stock Outward added successfully'}), 201

# Get all Stock Outwards
@app.route('/get_stos', methods=['GET'])
def get_stos():
    all_stos = StockOutward.query.all()
    return jsonify([sto.to_dict() for sto in all_stos]), 200

# Add Stock Inward
@app.route('/add_sti', methods=['POST'])
def add_sti():
    data = request.json
    new_sti = StockInward(
        sti_no=data.get('sti_no'),
        date=data.get('date'),
        shift=data.get('shift'),
        incharge=data.get('incharge'),
        referred_by=data.get('referred_by'),
        required_for=data.get('required_for'),
        purchase_type=data.get('purchase_type'),
        invoice_number=data.get('invoice_number'),
        sr_no=data.get('sr_no'),
        received_by=data.get('received_by'),
        purchase_party=data.get('purchase_party'),
        vehicle_no=data.get('vehicle_no'),
        material=data.get('material'),
        rate=data.get('rate'),
        mms_quantity=data.get('mms_quantity'),
        mains_gross=data.get('mains_gross'),
        mains_tare=data.get('mains_tare'),
        mains_net_quantity=data.get('mains_net_quantity'),
        gst=data.get('gst'),
        total_amount=data.get('total_amount'),
        mod_of_payment=data.get('mod_of_payment'),
        amount_paid=data.get('amount_paid'),
        balance=data.get('balance'),
        driver_mobile=data.get('driver_mobile'),
        driver_name=data.get('driver_name'),
        loading_site=data.get('loading_site'),
        unloading_site=data.get('unloading_site'),
        trip_amount=data.get('trip_amount'),
        beta_allowance=data.get('beta_allowance'),
        total_d_amount=data.get('total_d_amount'),
        d_mode_of_payment=data.get('d_mode_of_payment'),
        d_amount_paid=data.get('d_amount_paid'),
        d_balance=data.get('d_balance'),
        owner_mobile=data.get('owner_mobile')
    )
    db.session.add(new_sti)
    db.session.commit()
    return jsonify({'message': 'Stock Inward added successfully'}), 201


# Get all Stock Inwards
@app.route('/get_stis', methods=['GET'])
def get_stis():
    all_stis = StockInward.query.all()
    return jsonify([sti.to_dict() for sti in all_stis]), 200

@app.route('/add_payment_inward', methods=['POST'])
def add_payment_inward():
    data = request.json
    new_payment = PaymentInward(**data)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment Inward added successfully'}), 201

@app.route('/get_payment_inwards', methods=['GET'])
def get_payment_inwards():
    all_payments = PaymentInward.query.all()
    return jsonify([payment.to_dict() for payment in all_payments]), 200

@app.route('/add_payment_outward', methods=['POST'])
def add_payment_outward():
    data = request.json
    new_payment = PaymentOutward(**data)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment Outward added successfully'}), 201

@app.route('/get_payment_outwards', methods=['GET'])
def get_payment_outwards():
    all_payments = PaymentOutward.query.all()
    return jsonify([payment.to_dict() for payment in all_payments]), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Here, you should verify the username and password with your user model
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'JWT is working!'})