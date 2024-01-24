import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from model.utils import write_file
from config.config import get_settings
from model.test_model import prediction_for_a_file


origins = ["*"]

settings = get_settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None


@app.on_event("startup")
def startup_event():
    global model
    model = tf.keras.models.load_model(str(settings.MODEL_FILE))


@app.get("/")
def read_root():
    return {"message": "Welcome to the Noise Removal API"}


@app.post("/api/predict")
async def remove_noise(file: UploadFile = File(...)):
    try:
        print("Post request received", file.filename)
        write_file(file)
        output_file = prediction_for_a_file(
            file=file.filename,
            model=model,
        )
        return {
            "success": True,
            "data": f"{output_file}",
            "message": "Prediction completed",
        }
    except Exception as e:
        print(e)
        return {"success": False, "message": "Prediction failed", "data": None}
