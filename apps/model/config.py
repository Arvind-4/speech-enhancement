import pathlib
from functools import lru_cache


BASE_DIR = pathlib.Path(__file__).resolve(strict=True).parent.parent

MODEL_FILE = str(BASE_DIR) + "/" + "weights" + "/" + "model_unet.h5"

AUDIO_DIR_PREDICTION = str(BASE_DIR) + "/" + "test_data" + "/" + "test"
DIR_SAVE_PREDICTION = str(BASE_DIR) + "/" + "test_data" + "/" + "saved_predictions"


SAMPLE_RATE: int = 8000
MIN_DURATION: float = 1.0
FRAME_LENGTH: int = 8064
HOP_LENGTH_FRAME: int = 8064
N_FFT: int = 255
HOP_LENGTH_FFT: int = 63


class Settings:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


@lru_cache()
def get_settings():
    settings = Settings(
        SAMPLE_RATE=SAMPLE_RATE,
        MIN_DURATION=MIN_DURATION,
        FRAME_LENGTH=FRAME_LENGTH,
        HOP_LENGTH_FRAME=HOP_LENGTH_FRAME,
        N_FFT=N_FFT,
        HOP_LENGTH_FFT=HOP_LENGTH_FFT,
        BASE_DIR=BASE_DIR,
        MODEL_FILE=MODEL_FILE,
        AUDIO_DIR_PREDICTION=AUDIO_DIR_PREDICTION,
        DIR_SAVE_PREDICTION=DIR_SAVE_PREDICTION,
    )
    return settings
