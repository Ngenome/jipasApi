from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    fields =['title','note' ,'category', 'date_added']
    list_display=('title','date_added')
    search_fields=['title', 'category']
admin.site.register(Note, NoteAdmin)
