from django.urls import path
from.import views


app_name = 'login'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.second, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/', views.registration, name="registration"),

]