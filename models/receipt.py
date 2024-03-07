import uuid

from models.receipt_item import ReceiptItem
from datetime import datetime

class Receipt:
  def __init__(self, data):
    # Validate data
    self.validate_receipt_data(data)

    # Assign an id for the receipt
    self.id = str(uuid.uuid4())

    # Set provided values
    self.retailer = data['retailer']
    dt = datetime.strptime(data['purchaseDate'], "%Y-%m-%d")
    tm = datetime.strptime(data['purchaseTime'], "%H:%M").time()
    self.purchase_datetime = datetime.combine(dt, tm)
    self.items = []
    for item_data in data['items']:
      item = ReceiptItem(item_data)
      self.items.append(item)
    self.total = float(data['total'])

    # Instantiate points data
    self.points = 0
    self.points_breakdown = []

  def validate_receipt_data(self, data):
    if not isinstance(data, dict):
      raise ValueError("Receipt data must be a dictionary")

    required_fields = ['retailer', 'purchaseDate', 'purchaseTime', 'items', 'total']
    missing_fields = []
    for field in required_fields:
      if field not in data:
        missing_fields.append(field)
    if missing_fields:
        raise ValueError(f"Missing required field(s): {', '.join(missing_fields)}")

    if not isinstance(data['retailer'], str) or not data['retailer'].strip():
      raise ValueError("Retailer must be a non-empty string")

    if not isinstance(data['purchaseDate'], str) or not data['purchaseDate'].strip():
      raise ValueError("purchaseDate must be a non-empty string")

    if not isinstance(data['purchaseTime'], str) or not data['purchaseTime'].strip():
      raise ValueError("purchaseTime must be a non-empty string")

    if not isinstance(data['items'], list) or not data['items'] or not all(isinstance(item, dict) for item in data['items']):
      raise ValueError("items must be a non-empty list of dictionaries")

    for item in data['items']:
      if 'shortDescription' not in item or 'price' not in item:
        raise ValueError("Each item must have 'shortDescription' and 'price' fields")

      if not isinstance(item['shortDescription'], str) or not item['shortDescription'].strip():
        raise ValueError("Item shortDescription must be a non-empty string")

      if not isinstance(item['price'], str) or not item['price'].strip().replace('.', '').isdigit():
        raise ValueError("Item price must be a string representing a valid number")

    if not isinstance(data['total'], str) or not data['total'].strip().replace('.', '').isdigit():
      raise ValueError("Total must be a string representing a valid number")