class ReceiptItem:
    def __init__(self, data):
        self.shortDescription = data['shortDescription']
        self.price = float(data['price'])
