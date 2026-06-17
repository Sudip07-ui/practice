

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Contact
from .serializers import ContactSerializer


# API 1 - Create Contact
@api_view(['POST'])
def create_contact(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


# API 2 - Get All Contacts
@api_view(['GET'])
def get_contacts(request):

    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)

    return Response(serializer.data)


# API 3 - Get Single Contact
@api_view(['GET'])
def get_contact(request, pk):

    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response(
            {"error": "Contact not found"},
            status=404
        )

    serializer = ContactSerializer(contact)

    return Response(serializer.data)


# API 4 - Update Contact
@api_view(['PUT'])
def update_contact(request, pk):

    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response(
            {"error": "Contact not found"},
            status=404
        )

    serializer = ContactSerializer(
        contact,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# API 5 - Delete Contact
@api_view(['DELETE'])
def delete_contact(request, pk):

    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response(
            {"error": "Contact not found"},
            status=404
        )

    contact.delete()

    return Response(
        {"message": "Contact deleted successfully"},
        status=200
    )