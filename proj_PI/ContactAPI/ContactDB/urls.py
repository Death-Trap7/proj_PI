from django.urls import path
from .views import *

urlpatterns = [path("getContacts", getAll, name="contactlist"),
               path("createContact", createContacter, name="contactCreation"),
               path("getContactbyid/<int:id>", getContactID, name="contactid"),
               path("updateContact/<int:id>", updateContacter, name="update"),
               path("deleteContact/<int:id>", deleteContact, name="delete")
 ]
