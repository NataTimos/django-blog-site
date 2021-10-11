from django import template
from django.db.models import Count

register = template.Library()

from ..models import Post

@register.simple_tag  #возвращает строку
def total_posts():
    return Post.objects.filter(status ='published').count()

@register.inclusion_tag('blog/latest_posts.html') #возвращает словарь
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status='published').order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag  #assignment_tag is obsolete
def get_most_commented_posts(count=5):
    return Post.objects.filter(status='published').annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]