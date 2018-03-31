from django.contrib import admin

# Register your models here.


from django.contrib import admin
#from more_with_admin.examples import models.py
from pages.models import Document

admin.site.register(Document)

