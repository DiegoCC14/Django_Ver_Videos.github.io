"""Ver_Videos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include

from django.contrib.auth.decorators import login_required

from .views import Home , Api_Videos_User , Api_Top_Videos

urlpatterns = [
	path('home/', login_required( Home.as_view() ) , name="home"),
    path('api_videos/', login_required( Api_Videos_User.as_view() ) ),
    path('api_top_videos/', login_required( Api_Top_Videos.as_view() ) ),
    
]
