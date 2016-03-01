from django.conf.urls import url, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .models import Post
# art_category
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<art_category__Name>.+)/(?P<slug>.+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<art_category__Name>.+)/$', views.cat_post, name='cat_post'),
]