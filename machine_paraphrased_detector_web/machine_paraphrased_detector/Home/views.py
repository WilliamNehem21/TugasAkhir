from django.shortcuts import render
from .forms import HomeInput

# Create your views here.
def index(request):
    home_input = HomeInput()
    context = {
        'home_input' : home_input,
    }
    print(request.method)
    if (request.method == "POST"):
        return render(request, 'Home/output.html')
    else:
        return render(request, 'Home/base.html', context)

def output(request):
    return render(request, 'Home/output.html')