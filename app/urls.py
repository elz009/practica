from django.contrib import admin

from django.urls import include, path

app_name = 'name'
urlpatterns = [
    path('', admin.site.urls),
    path('', include('main.urls', namespace='main'))
]   
