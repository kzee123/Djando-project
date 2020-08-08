"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blogapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index.html',views.index),
    path('form.html',views.form),
    path('about.html',views.about),
    path('rooms.html',views.rooms),
    path('contact.html',views.contact),
    path('foodform.html',views.order),
    path('feedbackform.html',views.feedback1),
    path('insert.html',views.reserve),
    path('finsert.html',views.foodorder),
    path('feedinsert.html',views.feedback),

]


urlpatterns +=staticfiles_urlpatterns()

