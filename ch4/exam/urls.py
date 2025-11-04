from django.urls import path
from exam import views

urlpatterns=[
   path( 'view/',views.viewsIntemplate),
   path('dynamic/',views.dynamicTemplate),
   path('menu/',views.menu)
]