import pathlib
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from model.utils import write_file
from config.config import get_settings
from backend.utils import generate_data
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
        print("Output file", output_file)
        if output_file is None:
            return {"success": False, "message": "Prediction failed", "data": None}
        output_file_path = pathlib.Path(settings.DIR_SAVE_PREDICTION) / output_file
        input_file_path = pathlib.Path(settings.AUDIO_DIR_PREDICTION) / file.filename
        data = generate_data(input_file_path, output_file_path)
        print("Data generated", data)
        return {"success": True, "message": "Prediction successful", "data": data}

    except Exception as e:
        print(e)
        return {"success": False, "message": "Prediction failed", "data": None}
