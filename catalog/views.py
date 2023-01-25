from django.shortcuts import render
import datetime
# Create your views here.
from . models import Book, Author, BookInstance, Genre
from django.views import generic
from django.db.models import Count, Q

def index(request):
    now = datetime.datetime.now()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #available books are denoted with "a" in the status field
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'cur_time': now.strftime('%Y-%m-%d %H:%M:%S'),
    }

    return render(request, 'index.html', context=context) #render the html template index.html with the data in the context variable


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # your own name for the list as a template variable
    template_name = 'books/book_list.html'  # Specify your own template name/location

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'  # your own name for the list as a template variable
    template_name = 'authors/my_arbitrary_template_name_list.html'  # Specify your own template name/location



    def get_queryset(self):
        return Author.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        queryset = Book.objects.filter(author__in=Author.objects.filter())
        context['authored_books'] = queryset
        return context

class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        context['authored_books'] = "test"
        return context

    