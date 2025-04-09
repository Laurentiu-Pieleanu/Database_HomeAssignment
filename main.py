from fastapi import FastAPI, File, UploadFile, HTTPException 
from pydantic import BaseModel
from bson import ObjectId
from fastapi.responses import JSONResponse 
import motor.motor_asyncio 
app = FastAPI() 
# Connect to Mongo Atlas 
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://laurentiupieleanuf32520:NL2a9GEOkyJuvcX7@assignment.ki0vy5z.mongodb.net/?retryWrites=true&w=majority&appName=Assignment") 
db = client.multimedia_db 
class PlayerScore(BaseModel): 
    player_name: str 
score: int 

@app.post("/upload_sprite") 
async def upload_sprite(file: UploadFile = File(...)): 
# In a real application, the file should be saved to a storage service 
    content = await file.read() 
    sprite_doc = {"filename": file.filename, "content": content} 
    result = await db.sprites.insert_one(sprite_doc) 
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)} 

@app.post("/upload_audio") 
async def upload_audio(file: UploadFile = File(...)): 
    content = await file.read() 
    audio_doc = {"filename": file.filename, "content": content} 
    result = await db.audio.insert_one(audio_doc) 
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)} 

@app.post("/player_score") 
async def add_score(score: PlayerScore): 
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc) 
    return {"message": "Score recorded", "id": str(result.inserted_id)} 

def convert_id(document):
    document["_id"] = str(document["_id"])
    return document

@app.get("/sprites")
async def get_sprites():
    sprites = []
    async for sprite in db.sprites.find():
        sprites.append(convert_id(sprite))
    return sprites

@app.get("/audios")
async def get_audios():
    audios = []
    async for audio in db.audio.find():
        audios.append(convert_id(audio))
    return audios

@app.get("/scores")
async def get_scores():
    scores = []
    async for score in db.scores.find():
        scores.append(convert_id(score))
    return scores