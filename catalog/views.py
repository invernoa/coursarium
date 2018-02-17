from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from catalog.models import Course, Category, Language, Media

def index(request):
    courses = Course.objects.all().order_by('id')[1:10]
    categories = Category.objects.all()
    startingsoon = Course.objects.all().filter(status=2)
    courses_categories1 = Course.objects.all().filter(category=1)
    courses_categories2 = Course.objects.all().filter(category=2)
    courses_categories3 = Course.objects.all().filter(category=3)
    courses_categories4 = Course.objects.all().filter(category=4)
    courses_categories5 = Course.objects.all().filter(category=5)
    courses_categories6 = Course.objects.all().filter(category=6)
    courses_categories7 = Course.objects.all().filter(category=7)
    courses_categories8 = Course.objects.all().filter(category=8)
    courses_categories9 = Course.objects.all().filter(category=9)
    courses_categories10 = Course.objects.all().filter(category=1)

    #Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context = {'courses': courses, 'categories': categories, 'startingsoon': startingsoon,
                   'courses_categories1': courses_categories1, 'courses_categories2': courses_categories2,
                   'courses_categories3': courses_categories3,'courses_categories4': courses_categories4,
                   'courses_categories5': courses_categories5,'courses_categories6': courses_categories6,
                   'courses_categories7': courses_categories7,'courses_categories8': courses_categories8,
                   'courses_categories9': courses_categories9, 'courses_categories10': courses_categories10, },
    )



from django.views import generic


class CourseListView(generic.ListView):
    model = Course
    context_object_name = 'all_courses'
    queryset = Course.objects.all()
    template_name = 'catalog/course_list.htlm'




class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'catalog/course_detail.html'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
