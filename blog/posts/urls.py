# posts/urls.py

from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.PostListView.as_view(), name=None),
    path('create/', views.PostCreateView.as_view(), name=None),
    path('<int:pk>/', views.PostDetailView.as_view(), name=None),
    path('', views.CommentListView.as_view(), name=None),
    path('create-comment/', views.CommentCreateView.as_view(), name=None),
    path('<int:pk>/', views.CommentDetailView.as_view(), name=None),

]

