from django.contrib import admin
from .models import *
from ckeditor.fields import RichTextField



admin.site.register(Topic)
admin.site.register(Type)
admin.site.register(Question)
admin.site.register(Question_Bank)