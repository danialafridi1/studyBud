from django.contrib import admin # type: ignore

# Register your models here.
from .models import Room ,Message,Topic

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)