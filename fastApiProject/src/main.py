import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_data
from database.models import Message

app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_all_message():
    data = collection.find()

    return all_data(data)


@router.post("/")
async def create_message(new_message: Message):
    try:
        resp = collection.insert_one(dict(new_message))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error: {e}")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
