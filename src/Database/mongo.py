from pymongo import MongoClient

# using mongo db container network interface -- development only
connection_string = "mongo-py"

def get_db():
   try:
      print("Connecting to mongo db")
      client = MongoClient(connection_string)
      db = client['Tranding']
      return db, client
   except Exception as e:
      print("Error connecting to mongoDb {e}")
      raise RuntimeError("Failled to connect {e}")