
from django.contrib import admin
from django.urls import path, include

# from Polls_Virtual.Polls_Project import polls_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls_app.urls')),
]
