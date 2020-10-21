from django.contrib import admin

# Register your models here.

from .models import Topic
from .models import EntryForm

admin.site.register(Topic)
admin.site.register(EntryForm)