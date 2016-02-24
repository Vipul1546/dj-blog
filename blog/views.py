from django.shortcuts import render
from .models import Post
from .models import News
from .models import Category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.template.defaultfilters import slugify


# Create your views here. itle_slug = slugify(Post.objects.values('title'));
def post_list(request):
    posts = Post.get_latest_items()
    newss = News.objects.order_by('?')[:2]
    p_id = Post.objects.values_list("id")
    return render(request, 'blog/post_list.html', {'posts': posts, 'newss': newss, 'p_id': p_id})

#title="-".join(title.split())
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    #cat = get_object_or_404(Category, id = id)
    spost = Post.get_latest_items(except_ids = [post.id])
    mpost = Post.objects.order_by('?')
    return render(request, 'blog/post_detail.html', {'post': post,'spost': spost,'mpost': mpost})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
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