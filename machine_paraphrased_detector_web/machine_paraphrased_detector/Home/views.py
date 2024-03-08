from django.shortcuts import render
from .forms import HomeInput
import time
import pickle
from .predict import Predict

# Create your views here.
def index(request):
    home_input = HomeInput()
    context = {
        'home_input' : home_input,
    }
    print(request.method)
    if (request.method == "POST"):
        time.sleep(5)
        return predict(request)
    else:
        return render(request, 'Home/base.html', context)

def output(request):
    return render(request, 'Home/output.html')

def predict(request):
    text = request.POST['text']
    
    predict_model = Predict(text)
    predicted, similarity = predict_model.predict()
    if predicted == 0:
        return render(request, 'Home/notParaphrased.html')
    else:
        context = {
            'similarity' : similarity,
        }
        return render(request, 'Home/paraphrased.html', context)