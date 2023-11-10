from django.urls import path,re_path
from .import views
from .views import startpage 
urlpatterns=[

    path('message/',views.index),
    path('startpage/', startpage, name='startpage'),

    

]