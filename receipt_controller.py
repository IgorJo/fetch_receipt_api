from flask import Flask, request, jsonify
from api.receipt import Receipt
from api.receipt_processor import ReceiptProcessor

app = Flask(__name__)

@app.route("/receipts/process", methods=["POST"])
def process_receipt():
  try:
    data = request.get_json()
    receipt = Receipt(data)
    processor = ReceiptProcessor()
    processor.calculate_points(receipt)
    receipts[receipt.id] = receipt
    return jsonify({"id": receipt.id}), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 400

@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
  if receipt_id in receipts:
    return jsonify({"points": receipts[receipt_id].points})

  return jsonify({"error": "Receipt id not found"}), 404

receipts = {}

if __name__ == "__main__":
  app.run(debug=False)
