from fastapi.routing import APIRoute
from starlette.requests import Request
from motor.motor_asyncio import AsyncIOMotorClient

from src.main import app


@app.get("/")
async def mainpage() -> str:
    return "YOU ARE ON THE MAIN PAGE"


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict:
    return {"message": f"Hello321 {name}"}

# async def create_record(request: Request) -> dict:
#     mongo_client: AsyncIOMotorClient = request.app.state.mongo_client["test_database"]
#     await mongo_client.records.insert_one({"sample": "record"})
#     return {"Success": True}
#
#
# async def get_records(request: Request) -> list:
#     mongo_client: AsyncIOMotorClient = request.app.state.mongo_client["test_database"]
#     cursor = mongo_client.records.find({})
#     res = []
#     for document in await cursor.to_list(length=100):
#         document["_id"] = str(document["_id"])
#         res.append(document)
#     return res
