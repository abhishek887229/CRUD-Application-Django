"""
URL configuration for demmy2 project.

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
from django.urls import path,include
from demo1 import views as d1
from demo2 import views as d2
from demo3 import views as d3

urlpatterns = [
    path('admin/', admin.site.urls),
    path("one/",include('demo1.urls')),
    path("one/",include('demo2.urls')),
    path("one/",include('demo3.urls')),
]
