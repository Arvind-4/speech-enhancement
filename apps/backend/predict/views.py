import pathlib
import tensorflow as tf
from django.views import View
from functools import lru_cache
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from model.utils import write_file
from config.config import get_settings
from predict.utils import generate_data
from model.test_model import prediction_for_a_file

settings = get_settings()


@lru_cache()
def load_model():
    return tf.keras.models.load_model(str(settings.MODEL_FILE))

def test(request):
    return JsonResponse({'hello': 'world'})


class PredictView(View):
    model = load_model()
    
    @method_decorator(csrf_exempt)
    def post(self, request):
        file = request.FILES['file']
        write_file(file)
        output_file = prediction_for_a_file(
            file=file.filename,
            model=self.model,
        )
        print("Output file", output_file)
        if output_file is None:
            return {"success": False, "message": "Prediction failed", "data": None}
        output_file_path = pathlib.Path(settings.DIR_SAVE_PREDICTION) / output_file
        input_file_path = pathlib.Path(settings.AUDIO_DIR_PREDICTION) / file.filename
        data = generate_data(input_file_path, output_file_path)
        print("Data generated", data)

        return JsonResponse({'result': 'success', 'data': data, 'message': 'Prediction successful'})