from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()

@register.simple_tag
def cat_name(value):
  cat = Post(id=value).art_category.values('Name')
  for i in cat:
    return str(i.values())[3:-2]

@register.filter()
def cat_n(valuee):
  cat = Post(id=valuee).art_category.values('Name')
  for i in cat:
    return str(i.values())[3:-2]