from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
import datetime
# Create your tests here.

class PostTestCase(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='nareshdwivedi', email='naresh@gmail.com', password='testpassword')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')
    # Post.objects.create(title='', author='', text='', published_date='')

  def test_slug_generated(self):
    post = Post.objects.create(title='my name is naresh', author=self.user, text='ABCD EFGH IJKL', published_date=str(datetime.datetime.now()))
    self.assertEqual(post.slug, 'my-name-is-naresh')