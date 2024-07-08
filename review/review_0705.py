from fastapi import FastAPI, Query
from typing import Annotated
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()


@app.get("/")
def root():
    return {"Content": "This is the root"}


@app.get("/items/")
def read_items(item_id: int, q: Annotated[str | None, Query(max_length=50)] = None):
    result = {
        "items": [{"item_id": item_id}, {"item_id + 1": item_id + 1}]
    }
    if q:
        result.update({"q": q})
    return result

def generate_html_response():
    html_response = Path("./demo.html")
    return HTMLResponse(content=html_response, status_code=200)

@app.get("/html/")
def get_html():
    return generate_html_response()
# def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
