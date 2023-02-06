from django.db import models
from django.urls import reverse
# Create your models here.
import uuid # Required for unique book instances

#create a variable storing 10 different languages
LANGUAGES = (
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
    ('it', 'Italian'),
    ('de', 'German'),
    ('ru', 'Russian'),
    ('zh', 'Chinese'),
    ('ja', 'Japanese'),
    ('ko', 'Korean'),
    ('ar', 'Arabic'),
)

class Genre(models.Model): # model.Model is a class that represents a database table in Django
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name #returns the name of the genre


class Book(models.Model):
    title = models.CharField(max_length=200) # title is a field of the Book model
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,) # author is a field of the Book model
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book") #many to many relationship because a book can have many genres and a genre can have many books
    language = models.CharField(max_length=3, choices=LANGUAGES, blank=True, default='en', help_text='Book language')
    def __str__(self):
        return self.title

    def get_absolute_url(self): #the get_absolute_url method returns the url to access a particular instance of the model
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3]) #what does this do? This is a method that returns the first three genres of a book as a string separated by commas (for display purposes)


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def prefetch(self):
        return Book.objects.prefetch_related('author').filter(author=self.id)

    class Meta:
        ordering = ["last_name"]

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    
    def get_authored_books(self):
        return Book.objects.filter(author=self.id).count()
    
    def get_authored_books_list(self):
        return Book.objects.filter(author=self.id)

    




