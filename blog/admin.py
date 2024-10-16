from django.contrib import admin
from .models import Post
from .models import Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    # empty_value_display = "-empty-"
    # fields = ('title',)
    exclude = ("counted_view",)
    list_display = ("title",'author', "counted_view", "status", "published_date", "created_date",)
    list_filter = ('status','author')
    search_fields = ('title', 'content')
    
    
admin.site.register(Category)