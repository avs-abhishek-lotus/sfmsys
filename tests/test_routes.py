import unittest
from app import app, db

class RouteTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Inventory Management System', response.data.decode())

    def test_add_stock_requirement(self):
        # Assume JSON structure based on your StockRequirement fields
        response = self.client.post('/add_str', json={
            'str_no': 'STR002',
            'material': 'Steel',
            'material_quantity': 120,
            # other fields...
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Stock Requirement added successfully', response.data.decode())

if __name__ == '__main__':
    unittest.main()
