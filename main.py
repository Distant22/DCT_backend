from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from services import draw_service
from models import draw_model

app = FastAPI()

class User(BaseModel):
    name: str
    score: float

@app.post("/draw")
async def draw_building(user: User):
    try:
        image = await draw_service.calculate_image_type(user.score)
        await draw_model.draw_image(user.name, image)
        return "Success"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# uvicorn main:app --reload
