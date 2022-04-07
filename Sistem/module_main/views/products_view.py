from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Product
from ..serializes import ProductSerializers

@api_view(['GET','POST'])
def products_view(request):
    if request.method == 'GET':
        data_client = Product.objects.all();
        serialize = ProductSerializers(data_client, many= True)
        return Response(serialize.data)

    elif request.method == 'POST':
        new_serialize = ProductSerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def products_edit(request, id):
    try:
        data_prod = Product.objects.get(pk = id)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = ProductSerializers(data_prod)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_prod.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serialize = ProductSerializers(data_prod, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)