import unittest

from receipt_points.receipt_processor import ReceiptProcessor
from models.receipt import Receipt

class ReceiptProcessorTest(unittest.TestCase):
    def test_calculate_points(self):
        processor = ReceiptProcessor()
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
                {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
                {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
                {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
                {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
            ],
            "total": "35.35"
        }
        receipt = Receipt(receipt_data)
        processor.calculate_points(receipt)
        self.assertEqual(receipt.points, 28)

        receipt_data = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"}
            ],
            "total": "9.00"
        }
        receipt = Receipt(receipt_data)
        processor.calculate_points(receipt)
        self.assertEqual(receipt.points, 109)

if __name__ == '__main__':
    unittest.main()
