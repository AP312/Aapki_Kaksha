from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def login_page(request):
    return render(request,'login.html')

def tic_tac_toe(request):
    return render(request,'tic_tac_toe.html')

def meditation(request):
    return render(request,'meditation.html')

def memory_card(request):
    return render(request,'memory_card.html')

def draw(request):
    return render(request,'draw.html')

def basic_math(request):
    return render(request,'basic_math.html')

def read_news(request):
    return render(request,'read_news.html')
