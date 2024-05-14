import tornado.web
import tornado.httpclient

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    
    def options(self):
        # Autorise les pré-requêtes CORS pour toutes les méthodes HTTP
        self.set_status(204)
        self.finish()


class OrdersHandler(BaseHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        try:
            response = await client.fetch("http://api_orders:85/getOrders")
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write("HTTP Error: " + str(e))
        except Exception as e:
            self.write("An error occurred: " + str(e))

class PlatsHandler(BaseHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        try:
            response = await client.fetch("http://api_plats:8000/api/plats")
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write("HTTP Error: " + str(e))
        except Exception as e:
            self.write("An error occurred: " + str(e))

class OrdersByIdHandler(BaseHandler):
    async def get(self, order_id):
        client = tornado.httpclient.AsyncHTTPClient()
        try:
            # Construction de l'URL avec l'ID de commande
            url = f"http://api_orders:85/getOrdersById/{order_id}"
            response = await client.fetch(url)
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write(f"HTTP Error: {str(e)}")
        except Exception as e:
            self.write(f"An error occurred: {str(e)}")

class BeersRecommendationdHandler(BaseHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        try:
            # Construction de l'URL avec l'ID de commande
            url = f"http://api_beers:2711/recommandations"
            response = await client.fetch(url)
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write(f"HTTP Error: {str(e)}")
        except Exception as e:
            self.write(f"An error occurred: {str(e)}")


class BeersdHandler(BaseHandler):
    async def get(self):
        type = self.get_query_argument("type", default=None)
        min_abv = self.get_query_argument("min_abv", default=None)
        client = tornado.httpclient.AsyncHTTPClient()
        try:
            # Construction de l'URL avec l'ID de commande
            url = f"http://api_beers:2711/beers?type={type}&min_abv={min_abv}"
            response = await client.fetch(url)
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write(f"HTTP Error: {str(e)}")
        except Exception as e:
            self.write(f"An error occurred: {str(e)}")


