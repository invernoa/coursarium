from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Source
from .models import Category
from .models import Course

admin.site.register(Source)
admin.site.register(Course)
admin.site.register(Category)

