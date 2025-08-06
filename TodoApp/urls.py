from django.urls import path,include
from .views import Home,AddTask,Delete,Logout,Login,Register,TaskasExcel,Upload
urlpatterns = [
    path('',Home,name="Home"),
    path('AddTask/',AddTask,name="AddTask"),
    path('Delete/',Delete,name="Delete"),
    path('Logout/',Logout,name="Logout"),
    path('Login/',Login,name="Login"),
    path('Register/',Register,name="Register"),
    path('TaskasExcel/',TaskasExcel,name="TaskasExcel"),
    path('Upload/',Upload,name="Upload"),
        

]
