from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import easyocr
import shutil, os
from uuid import uuid4
import asyncio

app = FastAPI(title="KPay_Slip_OCR")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

reader = None

@app.on_event("startup")
async def preload_model():
    global reader
    loop = asyncio.get_event_loop()
    # preload the model (non-blocking startup)
    await loop.run_in_executor(None, lambda: easyocr.Reader(['en', 'my'], gpu=False))
    reader = easyocr.Reader(['en', 'my'], gpu=False)  # final model reference

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        filename = f"{uuid4()}.{file.filename.split('.')[-1]}"
        file_path = os.path.join(UPLOAD_DIR, filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = reader.readtext(file_path)
        os.remove(file_path)

        return JSONResponse(content={"result": [r[1] for r in result]})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
