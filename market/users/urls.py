from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'), 
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
    ]
