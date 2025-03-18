from django.shortcuts import render, redirect
from .models import Dish, TableBooking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now

def home_view(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant/home.html', {'dishes': dishes})

@login_required
def book_table(request):
    if request.method == "POST":
        table_number = request.POST.get("table_number")
        booking = TableBooking.objects.create(user=request.user, table_number=table_number, booking_time=now())
        return redirect('my_bookings')
    return render(request, 'restaurant/book.html')

@login_required
def my_bookings(request):
    bookings = TableBooking.objects.filter(user=request.user)
    return render(request, 'restaurant/my_bookings.html', {'bookings': bookings})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'restaurant/register.html', {'form': form})
