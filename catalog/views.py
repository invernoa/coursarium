from django.shortcuts import render

# Create your views here.
def course_list(request):
    return render(request, 'catalog/course_list.html', {})

from .models import Course, Source, Category

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_courses=Course.objects.all().count()
    
    num_sources=Source.objects.count()  # Метод 'all()' применен по умолчанию.
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_courses':num_courses,'num_sources':num_sources},
    )