from django.contrib import admin
from .models import post , author 

class postAdmin(admin.ModelAdmin):
    list_display = ['title','author','publish_date']
    list_filter = ['title','author','publish_date']
    search_fields = ['title','content']




admin.site.register(post,postAdmin)
admin.site.register(author)





# Register your models here.
