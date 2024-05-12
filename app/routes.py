from flask import request, jsonify, render_template, flash
from app import app, db
from app.models import StockRequirement, StockOutward, StockInward, PaymentInward, PaymentOutward
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/')
def index():
    return render_template('home.html')

# Endpoint for adding a new Stock Requirement
@app.route('/add_str', methods=['GET', 'POST'])
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
    else:
        # Assuming you have a form class or you just want to return a template
        return render_template('add_str_form.html')

@app.route('/get_strs', methods=['GET'])
def get_strs():
    all_strs = StockRequirement.query.all()
    return jsonify([str.to_dict() for str in all_strs]), 200

# Add Stock Outward
@app.route('/add_sto', methods=['GET', 'POST'])
def add_sto():
    if request.method == 'POST':
        data = request.json
        try:
            new_sto = StockOutward(
                required_for=data['required_for'],
                sales_type=data['sales_type'],
                invoice_number=data['invoice_number'],
                sr_no=data.get('sr_no', ''),  # Optional field with default
                issued_by=data['issued_by'],
                party=data['party'],
                vehicle_no=data['vehicle_no'],
                material=data['material'],
                rate=data['rate'],
                quantity=data['quantity'],
                gst=data['gst'],
                total_amount=data['total_amount'],
                mod_of_payment=data['mod_of_payment'],
                amount_paid=data['amount_paid'],
                balance=data['balance'],
                driver_mobile=data['driver_mobile'],
                owner_mobile=data['owner_mobile']
            )
            db.session.add(new_sto)
            db.session.commit()
            return jsonify({'message': 'Stock Outward added successfully'}), 201
        except KeyError as e:
            return jsonify({'error': f'Missing data for required field: {str(e)}'}), 400
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    else:
        # Assuming you have a form class or you just want to return a template
        return render_template('add_sto_form.html')

# Get all Stock Outwards
@app.route('/get_stos', methods=['GET'])
def get_stos():
    all_stos = StockOutward.query.all()
    return jsonify([sto.to_dict() for sto in all_stos]), 200

# Add Stock Inward
@app.route('/add_sti', methods=['GET', 'POST'])
def add_sti():
    if request.method == 'POST':
        data = request.json
        try:
            new_sti = StockInward(
                sti_no=data['sti_no'],
                date=data['date'],
                shift=data['shift'],
                incharge=data['incharge'],
                referred_by=data.get('referred_by', ''),  # Optional field with default
                required_for=data['required_for'],
                purchase_type=data['purchase_type'],
                invoice_number=data['invoice_number'],
                sr_no=data.get('sr_no', ''),  # Optional field
                received_by=data['received_by'],
                purchase_party=data['purchase_party'],
                vehicle_no=data['vehicle_no'],
                material=data['material'],
                rate=data['rate'],
                mms_quantity=data['mms_quantity'],
                mains_gross=data['mains_gross'],
                mains_tare=data['mains_tare'],
                mains_net_quantity=data['mains_net_quantity'],
                gst=data['gst'],
                total_amount=data['total_amount'],
                mod_of_payment=data['mod_of_payment'],
                amount_paid=data['amount_paid'],
                balance=data['balance'],
                driver_mobile=data['driver_mobile'],
                driver_name=data.get('driver_name', ''),  # Optional field
                loading_site=data['loading_site'],
                unloading_site=data['unloading_site'],
                trip_amount=data['trip_amount'],
                beta_allowance=data['beta_allowance'],
                total_d_amount=data['total_d_amount'],
                d_mode_of_payment=data['d_mode_of_payment'],
                d_amount_paid=data['d_amount_paid'],
                d_balance=data['d_balance'],
                owner_mobile=data['owner_mobile']
            )
            db.session.add(new_sti)
            db.session.commit()
            return jsonify({'message': 'Stock Inward added successfully'}), 201
        except KeyError as e:
            return jsonify({'error': f'Missing data for required field: {str(e)}'}), 400
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    else:
        # Assuming you have a form class or you just want to return a template
        return render_template('add_sti_form.html')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Username and password are required', 'error')
            return render_template('login.html')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Assuming you have a password check method
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            flash('Invalid credentials', 'error')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'JWT is working!'})

@app.route('/dashboard')
def dashboard():
    # Example: Fetch some data from your models
    total_stock_requirements = StockRequirement.query.count()
    total_stock_outward = StockOutward.query.count()
    total_stock_inward = StockInward.query.count()
    recent_inward = StockInward.query.order_by(StockInward.date.desc()).limit(5).all()  # Last 5 records
    recent_outward = StockOutward.query.order_by(StockOutward.date.desc()).limit(5).all()

    return render_template('dashboard.html',
                           total_stock_requirements=total_stock_requirements,
                           total_stock_outward=total_stock_outward,
                           total_stock_inward=total_stock_inward,
                           recent_inward=recent_inward,
                           recent_outward=recent_outward)
