from my_collection_demo.collection import MyCollection

collection = MyCollection()
collection.add_item("Book")
collection.add_item("Laptop")
collection.add_item("Pen")

collection.serialize("collection.pkl")
print("Collection serialized successfully.")
