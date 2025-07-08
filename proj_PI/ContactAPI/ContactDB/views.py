from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.
@api_view(["GET"])
def getAll(request):
    data = Contact.objects.all()
    serializedData = ContactSerializer(data, many=True)
    return Response(data=serializedData.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getContactID(request, id):
    data = Contact.objects.get(pk=id)
    serializedData = ContactSerializer(data)
    return Response(data=serializedData.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def createContacter(request):
    serializedData = ContactSerializer(data=request.data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(data=serializedData.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateContacter(request, id):
    staff = Contact.objects.get(pk=id)
    if staff:
        serializedData = ContactSerializer(staff, data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def deleteContact(request, id):
    data = Contact.objects.get(pk=id)
    if data:
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)
