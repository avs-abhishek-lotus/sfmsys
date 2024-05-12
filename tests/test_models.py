import unittest
from app import app, db
from app.models import StockRequirement, StockOutward

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_stock_requirement_creation(self):
        stock = StockRequirement(str_no="STR001", material="Wood", material_quantity=100)
        db.session.add(stock)
        db.session.commit()
        query = StockRequirement.query.get(stock.id)
        self.assertEqual(query.str_no, "STR001")

    def test_stock_outward_creation(self):
        stock = StockOutward(required_for="Sales", material="Metal", quantity=50)
        db.session.add(stock)
        db.session.commit()
        query = StockOutward.query.get(stock.id)
        self.assertEqual(query.required_for, "Sales")

if __name__ == '__main__':
    unittest.main()
