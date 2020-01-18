from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'rainbowApp/homePage.html',)

def contact(request):
    return render(request, 'rainbowApp/basic.html', {'values': ['Вопроси по телефону','(063) 572-17-48',
    'feo.englishclub@gmail.com']})


