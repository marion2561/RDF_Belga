import csv
from typing import List

from app.Order import Order
from app.OrderLine import OrderLine


def readOrdersFile():
    OrdersListLines : List[Order] = readOrdersLinesFile()
    OrdersList : List[Order] = []
    with open('app/Files/Orders.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                OrdersList.append(Order(row[3], row[0],row[2],row[1], filter_order_lines_by_order_no(OrdersListLines,row[3])))
            line_count+=1
    return OrdersList

def readOrdersLinesFile():
    OrdersListLines : List[Order] = []
    with open('app/Files/OrdersLines.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                # self, orderNo: int, LineNumber: int, ProductName:str, Quantity:int, UnitPrice: float, TotalLinePrice:float
                OrdersListLines.append(OrderLine(row[0], row[1],row[2],row[3],row[4],row[5]))
            line_count+=1
    return OrdersListLines

# Fonction pour filtrer les OrderLine par orderNo
def filter_order_lines_by_order_no(order_lines, order_no):
    return [line for line in order_lines if line.orderNo == order_no]