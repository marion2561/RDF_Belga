from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from app.FileReaderUtil import readOrdersFile
from app.Order import Order, serialiser_order

app = FastAPI()
#Liste des domaines autorisés, '*' signifie tout domaine
origins = [
    "http://localhost:4200",
    "http://localhost:81",
    "*",
]

# Configuration du middleware CORS                              
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Les origines autorisées
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PUT"],  # Les méthodes autorisées
    allow_headers=["X-Requested-With", "Content-Type"],  # Les en-têtes autorisés
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getOrders")
def getOrders():
    OrdersList : List[Order] = readOrdersFile()
    
    json_data = json.dumps(OrdersList, default=serialiser_order)
    print(json_data)
    return OrdersList

@app.get("/getOrdersById/{id}")
def getOrdersById(id:str):
    OrdersList : List[Order] = readOrdersFile()
    order: Order = [order for order in OrdersList if order.orderNo == id]
    json_data = json.dumps(order, default=serialiser_order)
    print(json_data)
    return order