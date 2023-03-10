import math

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from catalog.models import Person, Author, Book

from catalog.forms import TriangleForm, PersonForm, EmailForm
from catalog.task import send_email_task


class PersonListView(generic.ListView):
    template_name = 'person.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()


def triangle(request):
    if request.method == "POST":

        form = TriangleForm(request.POST)

        if request.POST.get('leg_1') and request.POST.get('leg_2') and form.is_valid():

            form.clean()

            leg_1 = form.cleaned_data.get('leg_1')
            leg_2 = form.cleaned_data.get('leg_2')
            gip = round(math.sqrt(leg_1**2 + leg_2**2), 2)

            return render(request, 'hypotenuse.html', {'gip': gip})

    else:
        form = TriangleForm()

    return render(request, 'triangle.html', {'form': form})


def person(request, person_id):
    return get_object_or_404(Person, pk=person_id)


def update_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('person'))
    else:
        form = PersonForm(instance=obj)

    return render(request, 'update_person.html', {'form': form, 'obj': obj})


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(reverse('index.html'))
    else:
        form = PersonForm()
    return render(request, 'create_person.html', {'form': form})


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.clean()
            print(form.cleaned_data['email'], form.cleaned_data['message'], form.cleaned_data['date_time'])
            send_email_task.apply_async(args=[form.cleaned_data['email'], form.cleaned_data['message']],
                                        eta=form.cleaned_data['date_time'])
            return redirect(reverse('send_email'))
    else:
        form = EmailForm()
    return render(request, 'email_form.html', {'form': form})


class AuthorListView(generic.ListView):
    template_name = 'author_list.html'
    context_object_name = 'author_list'
    paginate_by = 150
    model = Author
    queryset = Author.objects.prefetch_related('books').annotate(books_count=Count('books'))

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_list'
    paginate_by = 200
    model = Book
    queryset = Book.objects.annotate(authors_count=Count('authors'))

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
