from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='room_form'),
    path('update-room/<str:pk>/',views.updateRoom,name='update_room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete_room'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),

 ]