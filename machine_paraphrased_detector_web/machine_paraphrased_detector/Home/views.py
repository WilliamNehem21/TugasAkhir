from django.shortcuts import render
from .forms import HomeInput
import time

# Create your views here.
def index(request):
    home_input = HomeInput()
    context = {
        'home_input' : home_input,
    }
    print(request.method)
    if (request.method == "POST"):
        time.sleep(5)
        return render(request, 'Home/paraphrased.html')
    else:
        return render(request, 'Home/base.html', context)

def output(request):
    return render(request, 'Home/output.html')