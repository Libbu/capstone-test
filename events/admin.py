from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event
# Register your models here.


admin.site.register(Event)