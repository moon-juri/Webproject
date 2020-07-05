from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.WriterBlog)
class WriterBlogAdmin(admin.ModelAdmin):
    
    list_display = ('postTitle', 'postExp', 'postDate')

    search_fields = ['postTitle', ]

    fieldsets = (
        ("게시글정보", {
            "fields": ('postTitle', 'postExp'
                
            ),
        }),
    )
    