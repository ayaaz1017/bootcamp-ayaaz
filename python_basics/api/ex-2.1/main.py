from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Serve an HTML page with a list of items
@app.get("/")
async def home(request: Request):
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    return templates.TemplateResponse("items.html", {"request": request, "items": items})
