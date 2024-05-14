import json
import tornado.web
import tornado.httpclient
import urllib3
from urllib.parse import quote

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
            response = await client.fetch("http://api_plats:80/api/plats")
            data = response.body.decode()
            self.write(data)
        except tornado.httpclient.HTTPError as e:
            self.write("HTTP Error: " + str(e))
        except Exception as e:
            self.write("An error occurred: " + str(e))

class BestBeers(BaseHandler):
    def initialize(self):
        self.http = urllib3.PoolManager()

    async def get(self, mealName):
        try:
            encoded_mealName = quote(mealName)
            response = self.http.request('GET', f"http://api_ia_beers:89/getbestbeers/{encoded_mealName}")
            beers = json.loads(response.data.decode())

            merged_beer_info = await self.merge_beer_info(beers)

            self.write(json.dumps(merged_beer_info, indent=2, ensure_ascii=False))
        except urllib3.exceptions.HTTPError as e:
            self.write("HTTP Error: " + str(e))
        except Exception as e:
            self.write("An error occurred: " + str(e))

    async def get_beer_details(self, beer_id):
        url = f"http://api_beers:2711/beers?id={beer_id}"
        response = self.http.request('GET', url)
        details = json.loads(response.data.decode())
        if isinstance(details, list) and details:
            return details[0]
        else:
            raise ValueError("Unexpected response format")

    async def merge_beer_info(self, beer_json):
        merged_beer_info = []
        for beer in beer_json:
            beer_id = beer['Id']
            detailed_info = await self.get_beer_details(beer_id)
            merged_info = {
                "ABV": detailed_info.get("ABV"),
                "Brewery": detailed_info.get("Brewery"),
                "Description": detailed_info.get("Description"),
                "IBU": detailed_info.get("IBU"),
                "Id": detailed_info.get("Id"),
                "Image_URL": detailed_info.get("Image_URL"),
                "Name": detailed_info.get("Name"),
                "Type": detailed_info.get("Type"),
                "Explanation": beer.get("Explanation")
            }
            merged_beer_info.append(merged_info)
        return merged_beer_info


class MenuHandler(BaseHandler):
    def initialize(self):
        self.http = urllib3.PoolManager()

    async def get(self):
        try:
            response = self.http.request('GET', f"http://api_ia_menu:88/getMenu")
            beers = json.loads(response.data.decode())

            merged_beer_info = await self.merge_beer_info(beers)

            self.write(json.dumps(merged_beer_info, indent=2, ensure_ascii=False))
        except urllib3.exceptions.HTTPError as e:
            self.write("HTTP Error: " + str(e))
        except Exception as e:
            self.write("An error occurred: " + str(e))

    async def get_beer_details(self, beer_id):
        url = f"http://api_beers:2711/beers?id={beer_id}"
        response = self.http.request('GET', url)
        details = json.loads(response.data.decode())
        if isinstance(details, list) and details:
            return details[0]
        else:
            raise ValueError("Unexpected response format")

    async def merge_beer_info(self, beer_json):
        beer_json = beer_json[0]
        beer_id = beer_json['IdBeer']
        detailed_info = await self.get_beer_details(beer_id)
        merged_info = {
            "ABV": detailed_info.get("ABV"),
            "Brewery": detailed_info.get("Brewery"),
            "Description": detailed_info.get("Description"),
            "IBU": detailed_info.get("IBU"),
            "Id": detailed_info.get("Id"),
            "Image_URL": detailed_info.get("Image_URL"),
            "Name": detailed_info.get("Name"),
            "Type": detailed_info.get("Type"),
            "Explanation": beer_json.get("Explanation"),
            "IdMeal": beer_json.get("IdMeal"),
            "MealName": beer_json.get("MealName")
        }
        return merged_info

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


