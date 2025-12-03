from django.urls import path
from django.contrib import admin
from .views import (
    cars_list, books_list, person_list, asosiy_sahifa,
    book_detail, car_detail, person_detail
)

urlpatterns = [
    path('', asosiy_sahifa, name='home'),

    path('cars/', cars_list, name='cars'),
    path('cars/<int:id>/detail/', car_detail, name='car_detail'),

    path('books/', books_list, name='books'),
    path('books/<int:id>/detail/', book_detail, name='book_detail'),

    path('person/', person_list, name='person'),
    path('person/<int:id>/detail/', person_detail, name='person_detail'),

    path('admin/', admin.site.urls),
]
