from django.db import models

# Create your models here.
from django.db import models
#from uuid import uuid4


def generateUUID():
    return str(uuid4())
# Create your models here.


class Category(models.Model):
	"""
	Model representing a book genre (e.g. Science Fiction, Non Fiction).
	"""
	name = models.CharField(max_length=200, help_text="Enter a course category")
	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Course(models.Model):
	"""
	Model representing a course.
	"""
	id = models.CharField(primary_key=True, max_length=50, help_text="Unique ID for this particular course ")
	title = models.CharField(max_length=200)
	source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)
	# Foreign Key used because book can only have one sourse, but sources can have multiple courses
   
	summary = models.TextField(max_length=1000, help_text="Enter a brief description of the course")
	isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, help_text="Select a category for this course")
   
	# Category class has already been defined so we can specify the object above.
	
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.title
	
	
	def get_absolute_url(self):
		"""
		Returns the url to access a particular book instance.
		"""
		return reverse('course-detail', args=[str(self.id)])      

class Source(models.Model):
	name = models.CharField(max_length = 200)
	link = models.CharField(max_length = 200)     

	def get_absolute_url(self):
		"""
		Returns the url to access a particular author instance.
		"""
		return reverse('source-detail', args=[str(self.id)])
	

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return '{0} ({1})'.format (self.name, self.link)