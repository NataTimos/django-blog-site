from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post
from .forms import PostForm

# def post_list(request):
#     object_list = Post.objects.filter(status = "published")
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post_list.html', {'page': page, 'posts': posts})

class PostListView(ListView):
    queryset = Post.objects.filter(status = "published")
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                                   status = 'published',
                                   published_date__year = year,
                                   published_date__month = month,
                                   published_date__day = day)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(Post, id = post_id, status = 'published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.changed_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {
        'post': post,
        'form': form
    })
        


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False) # commit=False means that we don't want to save the Post model yet 
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#         return render(request, 'blog/post_edit.html', {'form':form})


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})