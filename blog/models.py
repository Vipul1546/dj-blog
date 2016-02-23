from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.db.models import Q

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text =  models.TextField()
  image = models.ImageField(upload_to='images',null=True)
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


def create_slug(sender, instance, **kwargs):
  if slugify(instance.title) != instance.slug:
    instance.slug = slugify(instance.title)
    instance.save()
post_save.connect(create_slug, sender=Post)


class News(models.Model):
  source = models.CharField(max_length=200)
  news_detail = models.TextField()

  def __unicode__(self):
    return self.source

  class Meta:
    verbose_name_plural = "News"


def get_in_list(data, attribute):
  return map(lambda x: x[attribute], data)
