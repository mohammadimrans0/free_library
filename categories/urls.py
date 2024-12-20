from django.urls import path
from . import views

urlpatterns = [
    path('add_category', views.AddCategoryView.as_view(), name='add_category'),
]