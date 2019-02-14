from django.shortcuts import render
from datetime import datetime
from random import randint

# Create your views here.

def main(request):
    # получение данных
    name = 'Django'
    t = datetime.now().strftime('%H:%M:%S')
    num = randint(100000, 999999)
    # формирование контескта
    context = {
        'name': name,
        'time': t,
        'number': num
    }
    # вывод шаблона
    return render(request, 'main.html', context)
