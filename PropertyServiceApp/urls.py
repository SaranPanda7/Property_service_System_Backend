from django.urls import path
from .views import login, verify_login, registration, verify_registration, update_user, all_users, dashboard



urlpatterns = [

    path('all_users/', all_users, name='all_users'),
    path('login/', login, name='login'),
    path('verify_login/', verify_login, name='verify_login'),
    path('registration/', registration, name='registration'),
    path('verify_registration/', verify_registration, name='verify_registration'),
    path('update_user/', update_user, name='update_user'),
    path('dashboard/', dashboard, name='dashboard'),
]
