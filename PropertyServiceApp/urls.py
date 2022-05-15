from django.urls import path
from .views import *


urlpatterns = [

    path('all_users/', all_users, name='all_users'),
    path('login/', login, name='login'),
    path('verify_login/', verify_login, name='verify_login'),
    path('registration/', registration, name='registration'),
    path('verify_registration/', verify_registration, name='verify_registration'),
    path('update_user/', update_user, name='update_user'),
    path('dashboard/', dashboard, name='dashboard'),
    path('service_request/', create_service_request, name='service_request'),
    path('fetch_service_requests_by_user_id/', fetch_service_requests_by_user_id,
         name='fetch_service_requests_by_user_id/'),
    path('fetch_service_requests_for_admin/', fetch_service_requests_for_admin,
         name='fetch_service_requests_for_admin/'),
    path('fetch_all_users/', fetch_all_users,
         name='fetch_all_users/'),
    path('assign_agent_for_service_request/', assign_agent_for_service_request,
         name='assign_agent_for_service_request/'),
    path('create_user/', create_user,
         name='create_user/'),

]
