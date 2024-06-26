import tornado.ioloop
from tornado.web import Application, RequestHandler

from OrdersHandler import BeersRecommendationdHandler, BeersdHandler, OrdersByIdHandler, OrdersHandler, PlatsHandler, BestBeers, MenuHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        
def make_app():
    app = Application([
        (r"/", MainHandler),
        (r"/getOrders", OrdersHandler),
        (r"/getOrdersById/([0-9]+)", OrdersByIdHandler),
        (r"/beers", BeersdHandler),
        (r"/recommandations", BeersRecommendationdHandler),
        (r"/plats", PlatsHandler),
        (r"/bestBeers/(.*)", BestBeers),
        (r"/menu", MenuHandler),
    ])
    return app



if __name__ == "__main__":
    app = make_app()
    app.listen(81)
    print("Server is running on http://localhost:81")
    tornado.ioloop.IOLoop.current().start()
