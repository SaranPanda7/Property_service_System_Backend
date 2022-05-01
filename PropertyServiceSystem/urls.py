from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PropertyServiceApp.urls')),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


admin.site.site_title  =  "PROPERTY SERVICE SYSTEM"
admin.site.site_header  =  "Property Service System" 
admin.site.index_title  =  "Property_Service_System"