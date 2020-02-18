from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name=None),
    path('create/', views.CategoryCreateView.as_view(), name=None),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name=None),

]
