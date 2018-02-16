from django.conf.urls import url
from django.urls import path
from catalog import views


urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^courses/$', views.CourseListView.as_view(), name='courses'),
url(r'^course/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course-detail'),
               url(r'^category/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category-detail'),
]
