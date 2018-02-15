from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from catalog.models import Course, Category, Language, Media

def index(request):
    courses = Course.objects.all().order_by('-id')[:9]
    #Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context = {'courses': courses},
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

