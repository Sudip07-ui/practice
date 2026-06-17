from django.urls import path
from . import views

urlpatterns = [

    path(
        'contacts/',
        views.get_contacts,
        name='contacts'
    ),

    path(
        'contacts/create/',
        views.create_contact,
        name='create-contact'
    ),

    path(
        'contacts/<int:pk>/',
        views.get_contact,
        name='contact'
    ),

    path(
        'contacts/update/<int:pk>/',
        views.update_contact,
        name='update-contact'
    ),

    path(
        'contacts/delete/<int:pk>/',
        views.delete_contact,
        name='delete-contact'
    ),
]