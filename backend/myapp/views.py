# app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.ml_model import model, CLASS_NAMES
import numpy as np
from PIL import Image
from io import BytesIO

@csrf_exempt
def hello(request):
    return JsonResponse({"message": "Hello Vedanth"})

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file part'}, status=400)

        file = request.FILES['file']
        image = read_file_as_image(file.read())
        img_batch = np.expand_dims(image, 0)

        predictions = model.predict(img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])

        return JsonResponse({
            'class': predicted_class,
            'confidence': float(confidence)
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.http import HttpResponse
def test_view(request):
    return HttpResponse("Test view working!")
