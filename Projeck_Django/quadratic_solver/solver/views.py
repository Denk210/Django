from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import math

def solve_quadratic(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = request.GET.get('c', 0)

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return render(request, 'index.html', {'error': 'Неверный ввод. Пожалуйста, введите числовые значения для a, b и c.'})

    equation = f'{a}x^2 + {b}x + {c} = 0'
    solution = ''

    if a == 0:
        if b == 0:
            if c == 0:
                solution = 'Бесконечное количество решений'
            else:
                solution = 'Нет решений'
        else:
            x = -c / b
            solution = f'x = {x}'
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            solution = f'\nДискриминант: D = b^2 - 4ac = {discriminant}\n\nКорни: x1 = {x1}, x2 = {x2}'
        elif discriminant == 0:
            x = -b / (2*a)
            solution = f'\nДискриминант: D = b^2 - 4ac = {discriminant}\n\nКорень: x = {x}'
        else:
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            solution = f'\nДискриминант: D = b^2 - 4ac = {discriminant}\n\nКомплексные корни: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i'

    return render(request, 'index.html', {'equation': equation, 'solution': solution})