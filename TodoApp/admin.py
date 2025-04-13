from django.contrib import admin
from .models import Todo
from django.contrib.admin import AdminSite


def Marked_as_Completed(modeladmin,request,queryset):
    queryset.update(completionStatus=True)
Marked_as_Completed.short_description = "Marks selected books as Completed"     

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    
    list_display=['id','user','Title','CompletionDate','completionStatus','IsDelete']
    list_filter=['user','Title','completionStatus']
    search_fields = ['user','Title','completionStatus']
    actions = [Marked_as_Completed]
    list_display_links = ['Title']
    list_editable = ['completionStatus']
    actions_on_top = True
    

    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),

        ('Task Information', {
            'fields': ('Title', 'Description')
        }),

        ('Completion Status', {
            'fields': ('CompletionDate', 'completionStatus')
        }),


        ('Delete',
        {
            'fields':('IsDelete',)
        }
        )
    )


