from io import BytesIO

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image

from predict import predict

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Please see /docs for API usage."}

@app.post("/eyes")
async def findDisease(eyePic: UploadFile = File(...)):
    try:
        image_data = await eyePic.read()
        image = Image.open(BytesIO(image_data)).convert("RGB")
    except:
        raise HTTPException(status_code=400, detail="Uploaded files is not a valid image")

    result = predict(image)
    return {"result": result}


