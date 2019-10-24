
from django.contrib import admin
from django.urls import path
from django.conf import settings
import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', jobs.views.home, name = 'home'),
]
