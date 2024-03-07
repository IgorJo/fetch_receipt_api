from models.receipt import Receipt
from . import point_rules

class ReceiptProcessor:

  def calculate_points(self, receipt: Receipt):
    # It is sufficient to hardcode the rule sets that 
    # need to be run given there is only one set. 
    # Future functionality might result in multiple sets
    # of rules based on some criteria (eg. role, level)
    # in which case we would want to pass a set of rules
    # to be run by the processor or a way for the processor
    # to determine which rule set to utilize.

    point_rules.assignRetailerNamePointRule(receipt)
    point_rules.assignTotalRoundPointRule(receipt)
    point_rules.assignTotalMultiplePointRule(receipt)
    point_rules.assignItemPairsPointRule(receipt)
    point_rules.assignItemDescriptionPointRule(receipt)
    point_rules.assignPurchaseDateOddPointRule(receipt)
    point_rules.assignPurchaseHourPointRule(receipt)
