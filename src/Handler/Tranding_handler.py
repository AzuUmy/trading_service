from http.server import BaseHTTPRequestHandler
from Database.mongo import get_db
import json

class RequestHandler(BaseHTTPRequestHandler):

#requesst based on the amount of likes on database
    def do_GET(self):
        try:

            db, client = get_db()
            collection = db['mainTranding']

            #perfoming query in here
           # data = list(collection.find().sort([("likes", -1)]).limit(3)) #can be filtered to whatever amount desired this sorts by the amount of likes

            #perfoming query in here to collect all data from database
            data = list(collection.find())

            # calculatess the values of likes an clicks to find the averrage number an return the 10 position based on the average -- algorithm of tranding data

            for  item in data:
                likes = item.get('likes', 0)
                clicks = item.get('clicks', 0)
                average = (likes + clicks) / 2
                item['average'] = average

            sorted_data = sorted(data, key=lambda x: x['average'], reverse=True)

            top_10_data = sorted_data[:10]

            #turn the data into a json format - in our case it means it can return data to our forward server
            json_data = json.dumps(top_10_data, default=str)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = json.dumps({'error': str(e)})
            self.wfile.write(error_message.encode('utf-8'))