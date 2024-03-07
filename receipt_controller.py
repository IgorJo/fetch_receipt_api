from flask import Flask, request, jsonify
from models.receipt import Receipt
from receipt_points.receipt_processor import ReceiptProcessor

app = Flask(__name__)

@app.route("/receipts/process", methods=["POST"])
def process_receipt():
  try:
    data = request.get_json()
    receipt = Receipt(data)
    ReceiptProcessor().calculate_points(receipt)
    receipts[receipt.id] = receipt
    return jsonify({"id": receipt.id}), 200
  except Exception as e:
    return jsonify({"error": "The receipt is invalid"}), 400

@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
  if receipt_id in receipts:
    return jsonify({"points": receipts[receipt_id].points}), 200

  return jsonify({"error": "No receipt found for that id"}), 404

receipts = {}

if __name__ == "__main__":
  app.run(debug=False)
