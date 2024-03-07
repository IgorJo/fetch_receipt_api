import math

from models.receipt import Receipt

# Assigns receipt points based on:
#   One point for every alphanumeric character in the retailer name.
def assignRetailerNamePointRule(receipt: Receipt):
    award = len( ''.join(char for char in receipt.retailer if char.isalnum()) )
    receipt.points += award
    receipt.points_breakdown.append(f"{award} points - retailer name has 6 characters")

# Assigns receipt points based on:
#   50 points if the total is a round dollar amount with no cents.
def assignTotalRoundPointRule(receipt: Receipt, award: int = 50):
    if math.floor(receipt.total) == receipt.total:
      receipt.points += award
      receipt.points_breakdown.append(f"{award} points - total is a round dollar amount")

# Assigns receipt points based on:
#   25 points if the total is a multiple of passed in value.
def assignTotalMultiplePointRule(receipt: Receipt, multiple: float = 0.25, award: int = 25):
    if receipt.total % multiple == 0:
      receipt.points += award
      receipt.points_breakdown.append(f"{award} points - total is a multiple of 0.25")

# Assigns receipt points based on:
#   5 points for every two items on the receipt.
def assignItemPairsPointRule(receipt: Receipt):
    award = 5 * (len(receipt.items) // 2)
    receipt.points += award
    receipt.points_breakdown.append(f"{award} points - {len(receipt.items)} items (2 pairs @ 5 points each)")

# Assigns receipt points based on:
#   If the trimmed length of the item description is a multiple of 3, 
#   multiply the price by 0.2 and round up to the nearest integer. 
#   The result is the number of points earned.
def assignItemDescriptionPointRule(receipt: Receipt):
    for item in receipt.items:
      stripped_description = item.shortDescription.strip()
      if len(stripped_description) % 3 == 0:
        award = int(math.ceil(float(item.price) * 0.2))
        receipt.points += award
        receipt.points_breakdown.append(f"{award} points - '{stripped_description}' is {len(stripped_description)} characters (a multiple of 3)")

# Assigns receipt points based on:
#   6 points if the day in the purchase date is odd.
def assignPurchaseDateOddPointRule(receipt: Receipt, award: int = 6):
    if receipt.purchase_datetime.weekday() % 2 != 0:
      receipt.points += award
      receipt.points_breakdown.append(f"{award} points - purchase day is odd")

# Assigns receipt points based on:
#   10 points if the time of purchase is after 2:00pm and before 4:00pm.
def assignPurchaseHourPointRule(receipt: Receipt, award: int = 10):
    purchase_hour = receipt.purchase_datetime.hour
    if 14 <= purchase_hour < 16:
      receipt.points += award
      receipt.points_breakdown.append(f"{award} points - {receipt.purchase_datetime.hour} is between 2:00pm and 4:00pm")
