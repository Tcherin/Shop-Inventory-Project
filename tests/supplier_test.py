import unittest

from models.supplier import Supplier

class Testsupplier(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("VIDEOS R US", "0776494323", True)

    def test_supplier_has_name(self):
        self.assertEqual("VIDEOS R US", self.supplier.name)

    def test_supplier_has_contact_number(self):
        self.assertEqual("0776494323", self.supplier.contact_number)

    def test_supplier_has_activity_status(self):
        self.assertEqual(True, self.supplier.activity)
        