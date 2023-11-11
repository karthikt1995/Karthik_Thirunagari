from django.urls import path,re_path
from .import views
from .views import startpage, contact_detail, create_contact
urlpatterns=[

    path('message/',views.index),
    path('startpage/', startpage, name='startpage'),
    path('contact_detail/<int:serial_number>/', contact_detail, name='contact_detail'),
    path('create_contact/', create_contact, name='create_contact'),

    

]