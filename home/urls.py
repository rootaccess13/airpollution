from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('calibrate/', calibrate, name="calibrate"),
    path('connection/', connection, name="connection")
]
