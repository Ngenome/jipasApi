from django.contrib import admin
from .models import Comment
from .models import Image

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    fields =['name','comment' , 'date_added']
    list_display=('name','date_added')
    search_fields=['name', 'comment']
admin.site.register(Comment, CommentAdmin)
admin.site.register(Image)