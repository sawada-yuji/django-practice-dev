from django.contrib import admin
#from .models import SampleModel

#admin.site.register(SampleModel)
# Register your models here.

from .models import Book
admin.site.register(Book)
