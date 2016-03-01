from django.conf.urls import url, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from models import Employee
# art_category
urlpatterns = [
    url(r'^$', views.index, name='index'),
]