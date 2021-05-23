from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'entries/home.html')

def index(request):
    return render(request, 'entries/add.html')