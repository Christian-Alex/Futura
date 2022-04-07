from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Delivery
from ..serializes import DeliverySerializers

@api_view(['GET','POST'])
def deliverys_view(request):
    if request.method == 'GET':
        data_deliver = Delivery.objects.all();
        serialize = DeliverySerializers(data_deliver, many= True)
        return Response(serialize.data)

    elif request.method == 'POST':
        new_serialize = DeliverySerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def deliverys_edit(request, id):
    try:
        data_deliver = Delivery.objects.get(pk = id)
    except Delivery.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = DeliverySerializers(data_deliver)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_deliver.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serialize = DeliverySerializers(data_deliver, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)