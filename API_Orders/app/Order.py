from datetime import date
from typing import List

from app.OrderLine import OrderLine



class Order:
    def __init__(self, orderNo: int, ClientName: str, Date:date, price:float, lines:List[OrderLine]):
        self.orderNo = orderNo
        self.ClientName = ClientName
        self.Date = Date
        self.price = price
        self.lines = lines


def serialiser_order(order):
    """Cette fonction convertit un objet Order en un dictionnaire."""
    if isinstance(order, Order):
        return {
            "orderNo": order.orderNo,
            "ClientName": order.ClientName,
            "Date": order.Date,  # Convertit la date en format ISO (chaîne)
            "price": order.price
        }
    raise TypeError("Type d'objet non sérialisable")