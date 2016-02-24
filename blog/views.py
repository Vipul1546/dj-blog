from django.shortcuts import render
from django import template
from .models import Post
from .models import News
from .models import Category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.template.defaultfilters import slugify
register = template.Library()

# Create your views here. itle_slug = slugify(Post.objects.values('title'));
def post_list(request):
    posts = Post.get_latest_items()
    newss = News.objects.order_by('?')[:2]
    #p_id = Post.objects.filter(art_category__Name='travel')
    category_l = Category.objects.order_by('Name')
    return render(request, 'blog/post_list.html', {'posts': posts, 'newss': newss, 'category_l':category_l})

#title="-".join(title.split())
def post_detail(request, slug , art_category__Name):
    post = get_object_or_404(Post, slug=slug, art_category__Name=art_category__Name)
    # p_id = Post.objects.filter(art_category__Name=art_category__Name)
    #cat = get_object_or_404(Category, id = id)
    spost = Post.get_latest_items(except_ids = [post.id])[:5]
    mpost = Post.objects.order_by('?')
    return render(request, 'blog/post_detail.html', {'post': post,'spost': spost,'mpost': mpost})

def cat_post(request, art_category__Name):
    p_id = Post.objects.filter(art_category__Name=art_category__Name).values()
    return render(request, 'blog/category.html', {'p_id':p_id})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})