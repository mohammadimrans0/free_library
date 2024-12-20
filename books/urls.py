from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddBookCreateView.as_view(), name='add_book'),
    path('details/<int:pk>/', views.DetailBookView.as_view(), name='book_details'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
]