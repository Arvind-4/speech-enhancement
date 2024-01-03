from fastapi import APIRouter, UploadFile, File

from model.utils import write_file
from model.test_model import prediction_for_a_file

router = APIRouter()
