from django.contrib import admin
from .models import Todo
# list_display = [Todo]
# admin.site.register(list_display)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=['id','user','Title','CompletionDate','completionStatus']


# admin.site.register(Todo,TodoAdmin)