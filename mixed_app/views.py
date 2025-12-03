from django.shortcuts import render, get_object_or_404
from .models import Cars, Books, Person

def asosiy_sahifa(request):
    return render(request, 'asosiy.html')


def cars_list(request):
    cars = Cars.objects.all()
    return render(request, 'cars.html', {'cars': cars})

def car_detail(request, id):
    car = get_object_or_404(Cars, id=id)
    return render(request, 'car_detail.html', {'car': car})

def books_list(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Books, id=id)
    return render(request, 'detail.html', {'book': book})


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

def person_detail(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, 'person_detail.html', {'person': person})