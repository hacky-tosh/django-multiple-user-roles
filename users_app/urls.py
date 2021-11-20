from django.urls import path
from users_app import views
urlpatterns = [
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('lowdash/',views.lowdashboard,name='dashboard2')

]
