from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<str:tag_slug>', views.post_list, name = 'post_list_by_tag'),
    # path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:year>/<int:month>/<int:day>/<str:post>', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/share', views.post_share, name= 'post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),

]
