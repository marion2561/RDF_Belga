import tornado.ioloop
from tornado.web import Application, RequestHandler
from tornado_swagger.setup import setup_swagger

from OrdersHandler import BeersRecommendationdHandler, BeersdHandler, OrdersByIdHandler, OrdersHandler

class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # Permet les requêtes de toutes origines
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # Pas besoin de définir un corps; les en-têtes sont automatiquement ajoutés par `set_default_headers`.
        self.set_status(204)
        self.finish()

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
    ])
    return app



if __name__ == "__main__":
    app = make_app()
    app.listen(81)
    print("Server is running on http://localhost:81")
    tornado.ioloop.IOLoop.current().start()
