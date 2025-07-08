from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import requests as req
from .forms import *

# Create your views here.
base_url = "http://127.0.0.1:4554/"


def home(request):
    return render(request, "Home.html")


def contact_List(request):
    data = req.get(base_url+"contacts/getContacts")
    return render(request, "Contacts.html", {"list":data.json()})


def create_contact(request):
    if request.method == "GET":
        contact_Form = ContactorForm()
        return render(request, "ContactorForm.html", {"forms":contact_Form})
    if request.method == "POST":
        formData = ContactorForm(request.POST)
        if formData.is_valid():
            jsonData = formData.cleaned_data
            messages.success(request, 'Contact added successfully.')
            res = req.post(base_url+"contacts/createContact", json=jsonData)
            if res.status_code == 201:
                return redirect("homepage")
            else:
                return HttpResponse(f"API ERROR: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error: {formData.errors}")


def update_contact(request, id):
    if request.method == "GET":
        jsonData = req.get(base_url+f"contacts/getContactbyid/{id}").json()
        contact_Form = ContactorForm(initial=jsonData)
        return render(request, "ContactorForm.html", {"forms":contact_Form})
    elif request.method == "POST":
        formData = ContactorForm(request.POST)
        if formData.is_valid():
            jsonData = formData.cleaned_data
            messages.success(request, 'Contact updated successfully.')
            res = req.put(base_url+f"contacts/updateContact/{id}", json=jsonData)
            if res.status_code == 200:
                return redirect("homepage")
            else:
                return HttpResponse(f"API Error: {res.text}", status=res.status_code)
        return HttpResponse(f"Form Error {formData.errors}")


def delete_contact(request, id):
    if request.method == "POST":
        res = req.delete(base_url+f"contacts/deleteContact/{id}")
        if res.status_code == 204:
            return redirect("ContactList")
        else:
            return HttpResponse(f"API ERROR: {res.status_code}")
