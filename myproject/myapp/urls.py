from django.urls import path
from django.contrib.auth import logout
from . import views

urlpatterns = [
    path(route='', view=views.login_view, name='login'),
    path(route='home/', view=views.home, name='home'),
    path(route='logout/', view=views.logout_view, name='logout'),
]