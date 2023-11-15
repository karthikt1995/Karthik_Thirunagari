from django.urls import path,re_path
from .import views
from .views import startpage, contact_detail, create_contact, update_contact, delete_contact
urlpatterns=[

    path('message/',views.index),
    path('startpage/', startpage, name='startpage'),
    path('contact_detail/<int:serial_number>/', contact_detail, name='contact_detail'),
    path('create_contact/', create_contact, name='create_contact'),


    path('update_contact/<int:serial_number>/', update_contact, name='update_contact'),
    #deletecontacturl

    path('delete_contact/<int:serial_number>/', delete_contact, name='delete_contact'),

    

]