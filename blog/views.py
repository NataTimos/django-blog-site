from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(status = "published")
    for i in posts:
        # print(i.text)
        print(i.published_date.year )
        print(i.get_absolute_url())
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                                   status = 'published',
                                   published_date__year = year,
                                   published_date__month = month,
                                   published_date__day = day)
    return render(request, 'blog/post_detail.html', {'post': post})


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