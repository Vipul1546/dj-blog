from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.db.models import Q


# def get_upload_file_name(instance, filename):
#     return "uploaded_files/%s_%s" %(str(time()).replace('.','_'), filename)
###### --- Category Model
class Category(models.Model):
  Name = models.CharField(max_length=200)
  Description = models.CharField(max_length=2000)

  class Meta:
    verbose_name_plural = "Categories"

  def __unicode__(self):
    return self.Name

###### --- Post Model
class Post(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text =  models.TextField()
  image = models.ImageField(upload_to='images',null=True)
  art_category = models.ManyToManyField(Category)
  created_date = models.DateTimeField(
      default=timezone.now)
  published_date = models.DateTimeField(
      blank=True, null=True)
  slug = models.CharField(max_length=2000, null=True, blank=True, default='')

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __unicode__(self):
    return self.title

  @classmethod
  def get_latest_items(cls, post_limit=5, except_ids=[]):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    if len(except_ids) != 0:
      posts = posts.filter(~Q(id__in=except_ids))
    return posts

###### --- Slug
def create_slug(sender, instance, **kwargs):
   if slugify(instance.title) != instance.slug:
     instance.slug = slugify(instance.title)
     instance.save()
post_save.connect(create_slug, sender=Post)

###### --- News Model
class News(models.Model):
  source = models.CharField(max_length=200)
  news_detail = models.TextField()

  def __unicode__(self):
    return self.source

  class Meta:
    verbose_name_plural = "News"



def get_in_list(data, attribute):
  return map(lambda x: x[attribute], data)


  ##queries
  ## 1. post authr nd imge url not working in cat page
  ## 2. slug error on same title
  ##
