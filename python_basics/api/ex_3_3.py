from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, category: str = None):
    return {"item_id": item_id, "category": category or "Not specified"}
