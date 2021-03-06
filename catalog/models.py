from django.db import models

# Create your models here.
from django.db import models
from django.templatetags.i18n import language
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Category(models.Model):
    category_name = models.CharField(max_length=28, blank=True, null=True, default=None)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Language(models.Model):
    language = models.CharField(max_length=20, blank=True, null=True, default=None)
    def __str__(self):
        return self.language


class Status(models.Model):
    status = models.CharField(max_length=28, blank=True, null=True, default=None)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Media(models.Model):
    picture = models.CharField(max_length=200, blank=True, null=True, default=None )

    def __str__(self):
        return self.picture
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"



class Course(models.Model):
    # Model representing a course.
    course_title = models.CharField(max_length=200, blank=True, null=True, default=None)
    summary = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,)
    link = models.CharField(max_length=128, null=True, default=None)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    image = models.OneToOneField(Media, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def get_absolute_url(self):
        # Returns the url to access a particular book instance.
        return reverse('course-detail', args=[str(self.id)])
