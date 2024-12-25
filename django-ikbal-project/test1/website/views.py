from django.shortcuts import render, HttpResponse
from datetime import datetime
from random import randint

def index_view(request):
    now = datetime.now()
    time = f'{now.hour}:{now.minute}'
    minutes = now.minute
    randnum = randint(1, 1000000)
    fruits = [
        'apple', 'banana', 'orange',
        'grape', 'kiwi', 'mango',
        'pear', 'peach', 'cherry'
    ]

    context = {
        'randnum': randnum,
        'time': time,
        'fruits': fruits,
        'minutes': minutes
    }

    return render(request, 'index.html', context)

def rainbow_view(request):
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)

    context = {
        'red': red,
        'green': green,
        'blue': blue,
    }

    return render(request, 'rainbow.html', context)