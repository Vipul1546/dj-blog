from django.contrib import admin
from .models import Post
from .models import News
from blog.forms import PostForm

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  exclude = ('slug',)
  form = PostForm

admin.site.register(Post, PostAdmin)
admin.site.register(News)

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        #js = ('js/admin/my_own_admin.js',)
        css = {
             'all': ('media/admin/my_own_admin.css',)
        }