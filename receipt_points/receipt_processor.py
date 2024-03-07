from models.receipt import Receipt
from . import point_rules

class ReceiptProcessor:

  def calculate_points(self, receipt: Receipt):
    point_rules.assignRetailerNamePointRule(receipt)
    point_rules.assignTotalRoundPointRule(receipt)
    point_rules.assignTotalMultiplePointRule(receipt)
    point_rules.assignItemPairsPointRule(receipt)
    point_rules.assignItemDescriptionPointRule(receipt)
    point_rules.assignPurchaseDateOddPointRule(receipt)
    point_rules.assignPurchaseHourPointRule(receipt)
