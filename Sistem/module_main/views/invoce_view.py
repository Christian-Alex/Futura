from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Invoce
from ..serializes import InvoceSerializers

@api_view(['GET','POST'])
def invoces_view(request):
    if request.method == 'GET':
        data_invoce = Invoce.objects.all();
        serialize = InvoceSerializers(data_invoce, many= True)
        return Response(serialize.data)

    elif request.method == 'POST':
        new_serialize = InvoceSerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def invoces_edit(request, id):
    try:
        data_invoce = Invoce.objects.get(pk = id)
    except Invoce.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = InvoceSerializers(data_invoce)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_invoce.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)