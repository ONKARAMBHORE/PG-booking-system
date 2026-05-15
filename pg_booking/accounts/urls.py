from django.urls import path
from .views import register_user, login_user, logout_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('register/', register_user, name='register'),

    path('login/', login_user, name='login'),

    path('logout/', logout_user, name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)