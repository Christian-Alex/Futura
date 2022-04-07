from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Client
from ..serializes import ClientSerializers

@api_view(['GET','POST'])
def clients_view(request):
    if request.method == 'GET':
        data_client = Client.objects.all();
        serialize = ClientSerializers(data_client, many= True)
        return Response(serialize.data)

    elif request.method == 'POST':
        new_serialize = ClientSerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def clients_edit(request, id):
    try:
        data_client = Client.objects.get(pk = id)
    except Client.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = ClientSerializers(data_client)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_client.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serialize = ClientSerializers(data_client, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)