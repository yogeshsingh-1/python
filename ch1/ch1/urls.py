"""
URL configuration for ch1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from testapp import views as testapp
from exam import views as exam

urlpatterns = [
    path('admin/', admin.site.urls),
# testapp views
    path("welcome/",testapp.greetings),
    path("contact/",testapp.contact),
    path("about/",testapp.about),
# exam views
    path("science/",exam.science),
    path("math/",exam.math)

]
