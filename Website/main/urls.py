from django.urls import path
from . import views as v

urlpatterns = [
    path('login/', v.loginPage, name="login"),
    path('logout/', v.logoutUser, name="logout"),
    path('register/', v.registerPage, name="register"),

    path("", v.home, name="home"),
    path("room/<str:pk>/", v.room, name="room"),

    path('create-room/', v.createRoom, name="create-room"),
    path('update-room/<str:pk>', v.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', v.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>', v.deleteMessage, name="delete-message"),

]