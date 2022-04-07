from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Categorie
from ..serializes import CategoriesSerializers

@api_view(['GET','POST'])
def categories_view(request):
    if request.method == 'GET':
        data_cates = Categorie.objects.all();
        serialize = CategoriesSerializers(data_cates, many= True)
        return Response(serialize.data)

    elif request.method == 'POST':
        new_serialize = CategoriesSerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def categories_edit(request, id):
    try:
        data_cates = Categorie.objects.get(pk = id)
    except Categorie.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = CategoriesSerializers(data_cates)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_cates.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serialize = CategoriesSerializers(data_cates, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)
