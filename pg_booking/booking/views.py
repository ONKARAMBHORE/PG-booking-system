from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import BOOKING
from pgapp.models import PG
from django.contrib import messages
# Create your views here.


@login_required
def book_pg(request, pg_id):

    pg=PG.objects.get(id=pg_id)

    booking = BOOKING.objects.create(user=request.user, pg=pg)

    messages.success(request, "PG booked successfully!")

    return redirect('my_bookings')


def my_bookings(request):

    bookings = BOOKING.objects.filter(user=request.user)

    return render(request, 'my_bookings.html', {'bookings': bookings})

