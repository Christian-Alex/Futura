from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from module_main.models import Client, Product
from module_main.serializes import ForLogin

@api_view(['GET'])
def verifyClient(request, id):
    try:
        data_prod = Client.objects.get(pk = id)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = ForLogin(data_prod)
        return Response(serialize.data)