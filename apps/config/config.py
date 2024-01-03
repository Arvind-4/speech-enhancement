import pathlib
from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve(strict=True).parent.parent
    MODEL_FILE: str = str(BASE_DIR) + "/" + "weights" + "/" + "model_unet.h5"
    AUDIO_DIR_PREDICTION: str = str(BASE_DIR) + "/" + "test_data" + "/" + "test"
    DIR_SAVE_PREDICTION: str = str(BASE_DIR) + "/" + "test_data" + "/" + "saved_predictions"
    SAMPLE_RATE: int = 8000
    MIN_DURATION: float = 1.0
    FRAME_LENGTH: int = 8064
    HOP_LENGTH_FRAME: int = 8064
    N_FFT: int = 255
    HOP_LENGTH_FFT: int = 63


@lru_cache()
def get_settings():
    settings = Settings()
    return settings
