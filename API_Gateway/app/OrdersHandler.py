import tornado.web
import tornado.httpclient

class OrdersHandler(tornado.web.RequestHandler):
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



class OrdersByIdHandler(tornado.web.RequestHandler):
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

class BeersRecommendationdHandler(tornado.web.RequestHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        try:
            # Construction de l'URL avec l'ID de commande
            url = f"http://rdf-beers:2711/recommandations"
            response = await client.fetch(url)
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write(f"HTTP Error: {str(e)}")
        except Exception as e:
            self.write(f"An error occurred: {str(e)}")


class BeersdHandler(tornado.web.RequestHandler):
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


