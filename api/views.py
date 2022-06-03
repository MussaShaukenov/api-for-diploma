from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'api/base.html')
    

def get(request):
    return render(request, 'api/get.html')