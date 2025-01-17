"""
URL configuration for learnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#########AAAAAA##########
from firstApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #######AAAAAAA###########
    path('about-page/',views.about),
    path('about-show/',views.show),
    path('',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('kfc/',views.kfc),
    path('students/',views.students),
    path('books/',views.books,name='book'),
    path('book1/',views.book1,name='book1'),
    path('product/',views.product,name='product'),
    path('employee/',views.employee,name='employee'),
    path('class-based-view/',views.MyView.as_view(),name="class-based-view"),
    path('filters/',views.learnFilters),
    
]
