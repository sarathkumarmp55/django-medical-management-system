"""
URL configuration for medicalmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medical import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login',views.userlogin),
    path('about/',views.about),
    path('contact/',views.contactform),
    path('userhome/',views.userhome),
    path('medicine/',views.medicineshow),
    path('signup/',views.signup),
    path('order/',views.orders),
    path('orderdetails/',views.orderdetails),
    path('orderdetails/<id>',views.delet)

]
