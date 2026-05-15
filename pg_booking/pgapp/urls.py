from django.urls import path
from .views import pg_list, pg_detail, update_pg, delete_pg
from .views import add_pg
from .views import add_review

urlpatterns = [
    path('', pg_list, name='pg_list'),

    path('pg/<int:id>/', pg_detail, name='pg_detail'),

    path('add_pg/', add_pg, name='add_pg'),

    path('update-pg/<int:id>/', update_pg, name='update_pg'),

    path('delete-pg/<int:id>/', delete_pg, name='delete_pg'),

    path('add_review/<int:pg_id>/', add_review, name='add_review'),
    
]