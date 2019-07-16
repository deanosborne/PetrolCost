from django.urls import *
from django.conf.urls import *
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TagIndexView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('deals/', PostListView.as_view(), name='deals'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged')

]
