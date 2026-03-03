from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel




from fastapi.responses import HTMLResponse
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/Home")
def show_home():
    return {"this is first my end point"}

@app.get("/html/", response_class=HTMLResponse) ## end point= after/
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
            
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <button>submit</button>
        </body>
    </html>
    """

@app.get("/login", response_class=HTMLResponse)
def information_login():
    return """
    <html>
         <head>
            <title>Some HTML in here</title>
            
        </head>
        <body>
            <h1>Login page</h1>
            <input type="text" id="fname" name="Username"><br><br>
             <input type="text" id="fname" name="Password"><br><br>
            <button>submit</button>
            
        </body>
    </html>
    """

class Item(BaseModel):
    title:str = "New Brand"
    timestamp: datetime
    description: str | None = "this is first product"



@app.put("/product/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)    
           
