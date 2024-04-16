class OrderLine:
    def __init__(self, orderNo: int, LineNumber: int, ProductName:str, Quantity:int, UnitPrice: float, TotalLinePrice:float):
        self.orderNo = orderNo
        self.LineNumber = LineNumber
        self.ProductName = ProductName
        self.Quantity = Quantity
        self.UnitPrice = UnitPrice
        self.TotalLinePrice = TotalLinePrice

def serialiser_order_line(order_line):
    """Cette fonction convertit un objet OrderLine en un dictionnaire."""
    if isinstance(order_line, OrderLine):
        return {
            "orderNo": order_line.orderNo,
            "LineNumber": order_line.LineNumber,
            "ProductName": order_line.ProductName,
            "Quantity": order_line.Quantity,
            "UnitPrice": order_line.UnitPrice,
            "TotalLinePrice": order_line.TotalLinePrice
        }
    raise TypeError("Type d'objet non sérialisable")