from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Order
from ..serializes import OrderSerializers

@api_view(['GET','POST'])
def orders_view(request):
    if request.method == 'GET':
        data_order = Order.objects.all();
        serialize = OrderSerializers(data_order, many= True)
        return Response(serialize.data)

    elif request.method == 'POST':
        new_serialize = OrderSerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def orders_edit(request, id):
    try:
        data_order = Order.objects.get(pk = id)
    except Order.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = OrderSerializers(data_order)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_order.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)