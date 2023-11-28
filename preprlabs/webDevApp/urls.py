from django.urls import path
from .import views

#urls for pages
urlpatterns = [
    # path('', views.dashPage, name="dashboard"),
    path('', views.loginPage, name="login"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('dashboard/',views.dashPage, name="dashboard"),
    path('create-project/', views.createProjectPage , name="createProject"),
    path('user-data/', views.userDataPage, name="userData"),
]