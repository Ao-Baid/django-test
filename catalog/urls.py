from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #this is the path to the index page
    path('books/', views.BookListView.as_view(), name='books'), #this is the path to the books page
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), #this is the path to the book detail page
]