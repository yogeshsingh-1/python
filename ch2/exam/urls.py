from django.urls import path
from exam import views

urlpatterns = [
   path('science/',views.science),
   path('math/',views.math)
]