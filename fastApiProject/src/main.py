import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection_message
from database.schemas import all_data
from database.models import Message

app = FastAPI()
router = APIRouter()


@router.get("/api/v1/messages/")
async def get_all_message():
    data = collection_message.find()

    return all_data(data)


@router.post("/api/v1/message/")
async def create_message(new_message: Message):
    try:
        message_dict = new_message.dict()
        from_f_dict = new_message.from_f.to_dict()
        message_dict["from_f"] = from_f_dict
        resp = collection_message.insert_one(message_dict)
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error: {e}")


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
