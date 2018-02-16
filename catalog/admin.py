from django.contrib import admin

from django.contrib import admin
from .models import Course, Category, Language, Status, Media



admin.site.register(Language)
admin.site.register(Status)

class CourseAdmin(admin.ModelAdmin):

    list_display = ["id", "course_title", "category", "language"]
    list_filter = ["category", "language"]
    search_fields = ["course_title"]

    class Meta:
        model = Course

admin.site.register(Course, CourseAdmin)

class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "picture"]

    class Meta:
        model = Media

admin.site.register(Media,MediaAdmin )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "category_name"]

    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)