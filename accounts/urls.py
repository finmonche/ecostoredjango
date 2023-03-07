from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),

    path('forgetPassword/', views.forgetpassword, name="forget"),
    path('updatepassword/', views.updatepassword, name="updatepassword"),
]