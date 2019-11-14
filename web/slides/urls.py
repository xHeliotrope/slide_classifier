"""slides URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from classifier.views import HomeView
from classifier.views import SlideView
from classifier.views import SlideDataView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="homepage"),
    path("hash_word/<str:word>", HomeView.as_view(), name="homepage2"),
    path("slide", SlideView.as_view(), name="slide"),
    path("slide/data", SlideDataView.as_view(), name="slide_data"),
]
