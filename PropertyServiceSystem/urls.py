from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PropertyServiceApp.urls')),
]


admin.site.site_title = "PROPERTY SERVICE SYSTEM"
admin.site.site_header = "Property Service System"
admin.site.index_title = "Property_Service_System"
