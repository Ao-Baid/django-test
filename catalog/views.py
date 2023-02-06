from django.shortcuts import render
import datetime
# Create your views here.
from . models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logged_out.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


@login_required
def index(request):
    now = datetime.datetime.now()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #available books are denoted with "a" in the status field
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
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

    