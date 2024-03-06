from datetime import datetime
from .receipt import Receipt
import math

class ReceiptProcessor:

  def calculate_points(self, receipt: Receipt):
    points = 0
    points_breakdown = []

    # Points for retailer name
    award = len( ''.join(char for char in receipt.retailer if char.isalnum()) )
    points += award
    points_breakdown.append(f"{award} points - retailer name has 6 characters")

    # Points for total being a round dollar amount
    if math.floor(float(receipt.total)) == float(receipt.total):
      award = 50
      points += award
      points_breakdown.append(f"{award} points - total is a round dollar amount")

    # Points for total being a multiple of 0.25
    if float(receipt.total) % 0.25 == 0:
      award = 25
      points += award
      points_breakdown.append(f"{award} points - total is a multiple of 0.25")


    # Points for item pairs
    award = 5 * (len(receipt.items) // 2)
    points += award
    points_breakdown.append(f"{award} points - {len(receipt.items)} items (2 pairs @ 5 points each)")

    # Points for specific item descriptions
    for item in receipt.items:
      stripped_description = item["shortDescription"].strip()
      if len(stripped_description) % 3 == 0:
        award = int(math.ceil(float(item["price"]) * 0.2))
        points += award
        points_breakdown.append(f"{award} points - '{stripped_description}' is {len(stripped_description)} characters (a multiple of 3)")

    # Points for purchase date being odd
    if datetime.strptime(receipt.purchase_date, "%Y-%m-%d").weekday() % 2 != 0:
      award = 6
      points += award
      points_breakdown.append(f"{award} points - purchase day is odd")

    # Points for purchase time
    purchase_hour = int(receipt.purchase_time.split(":")[0])
    if 14 <= purchase_hour < 16:
      award = 10
      points += award
      points_breakdown.append(f"{award} points - {receipt.purchase_time} is between 2:00pm and 4:00pm")

    receipt.points = points
    receipt.points_breakdown = points_breakdown
