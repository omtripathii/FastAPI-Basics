# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/hello")
# async def hello(name: str = "World"):
#     return {"Well": f"Hello + {name}"}


# @app.get("/hello/{id}")
# async def hello(name: str = "World", id: int = 0):
#     return {"Well": {f"Hello + {name}", f"Your Id number is {id}"}}


# @app.get("/hello/{id}/me/")
# async def hello(name: str = "World", id: int = 0, lover: str | None = None):
#     return {"Well": {f"Hello + {name}", f"Your Id number is {id}",f'Your Lover is {lover}'}}

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    Roll_no: int


app = FastAPI()


@app.patch("/items/{i_id}")
async def main(i_id: int, item: Item):
    return {"ItemId": i_id, **item.dict()}
