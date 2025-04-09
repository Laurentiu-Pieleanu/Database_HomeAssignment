from fastapi import FastAPI, File, UploadFile, HTTPException 
from pydantic import BaseModel, Field
from typing import Annotated
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

# does not allows the user to use restricted characters when submiting the player name, as well as the player score has a specific range which
# cannot be exceeded
class PlayerScore(BaseModel):
    player_name: Annotated[str, Field(mid_lenght=1,max_length=50,pattern=r"^[a-zA-Z0-9_ ]+$")]
    score: Annotated[int, Field(ge=0,le=100000)]

# allows user to upload sprites on the database
@app.post("/upload_sprite") 
async def upload_sprite(file: UploadFile = File(...)): 
# In a real application, the file should be saved to a storage service 
    # the POST endpoint reads the file as binary using file.read() 
    content = await file.read()
    #creates a document which contains the filename and binary content
    sprite_doc = {"filename": file.filename, "content": content} 
    # document is pushed on the database
    result = await db.sprites.insert_one(sprite_doc) 
    # returns the unique id that is given to the document
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)} 

# allows user to upload audios on the database
@app.post("/upload_audio") 
async def upload_audio(file: UploadFile = File(...)): 
    # the POST endpoint reads the file as binary using file.read() 
    content = await file.read() 
    #creates a document which contains the filename and binary content
    audio_doc = {"filename": file.filename, "content": content} 
    # document is pushed on the database
    #if response is 200 OK is means success otherwise if is 400 Bad Request it is a failure
    result = await db.audio.insert_one(audio_doc) 
    # returns the unique id that is given to the document
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)} 

# allows user to upload players names and their scores on the database
@app.post("/player_score") 
async def add_score(score: PlayerScore): 
    #endpoint receives data in JSON format
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc) 
    return {"message": "Score recorded", "id": str(result.inserted_id)} 

#this function converts the ObjectId for the _id field into string
def convert_id(document):
    document["_id"] = str(document["_id"])
    return document

# allows user to get the sprites collection and what is inside
@app.get("/sprites")
async def get_sprites():
    #created empty lists that fill hold hte sprites from MongoDB
    sprites = []
    # a loop that fatched all the documents from the collection
    async for sprite in db.sprites.find():
        sprites.append(convert_id(sprite))
    return sprites

# allows user to get the audios collection and what is inside
@app.get("/audios")
async def get_audios():
    #created empty lists that fill hold hte sprites from MongoDB
    audios = []
    # a loop that fatched all the documents from the collection
    async for audio in db.audio.find():
        audios.append(convert_id(audio))
    return audios

# allows user to get the scores collection and what is inside
@app.get("/scores")
async def get_scores():
    #created empty lists that fill hold hte sprites from MongoDB
    scores = []
    # a loop that fatched all the documents from the collection
    async for score in db.scores.find():
        scores.append(convert_id(score))
    return scores