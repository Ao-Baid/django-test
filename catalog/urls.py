from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'), #this is the path to the index page
    path('books/', views.BookListView.as_view(), name='books'), #this is the path to the books page
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), #this is the path to the book detail page
    path('authors/', login_required(views.AuthorListView.as_view()), name='authors'), #this is the path to the authors page
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'), #this is the path to the author detail page
    
]