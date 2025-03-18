from django.urls import path
from .views import home_view, book_table, my_bookings, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('book/', book_table, name='book'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('register/', register_view, name='register'),
]
