from django import forms
#from django.db.models import get_model
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blog.models import Post
from django.db import models
from django.utils import timezone

class PostForm(forms.ModelForm):
  author = models.ForeignKey('auth.User')
  title = forms.CharField(max_length=200)
  text = forms.CharField(widget=CKEditorUploadingWidget())
  image = models.ImageField(upload_to='images',null=True)
  created_date = models.DateTimeField(
      default=timezone.now)
  published_date = models.DateTimeField(
      blank=True, null=True)
  slug = models.CharField(max_length=2000, null=True, blank=True, default='')

  class Meta:
      model = Post
      fields = "__all__"