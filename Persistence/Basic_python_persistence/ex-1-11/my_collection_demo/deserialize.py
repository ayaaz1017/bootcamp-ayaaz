from my_collection_demo.collection import MyCollection

collection = MyCollection.deserialize("collection.pkl")
print("Deserialized Collection:", collection.items)
