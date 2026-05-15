from django.urls import path
from .views import book_pg, my_bookings

urlpatterns = [

    path('book/<int:pg_id>/', book_pg, name='book_pg'),

    path('my_bookings/', my_bookings, name='my_bookings'),
]