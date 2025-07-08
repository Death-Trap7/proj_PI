from django.urls import path
from .views import *


urlpatterns = [
    path('' ,home, name='homepage'),

    path("createcontact", create_contact, name="create"),
    path("contactlist", contact_List, name= "ContactList"),

    path("updateContact/<int:id>", update_contact, name = "update"),
    path("deleteContact/<int:id>", delete_contact, name = "delete"),


]