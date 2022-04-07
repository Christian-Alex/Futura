from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Document
from ..serializes import DocumentsSerializers

@api_view(['GET','POST'])
def document_view(request):
    if request.method == 'GET':
        data_doc = Document.objects.all();
        serialize = DocumentsSerializers(data_doc, many= True)
        return Response(serialize.data)
    
    elif request.method == 'POST':
        new_serialize = DocumentsSerializers(data = request.data)
        if new_serialize.is_valid():
            new_serialize.save()
            return Response(new_serialize.data, status=status.HTTP_201_CREATED)
        return Response(new_serialize.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def documents_edit(request, id):
    try:
        data_doc = Document.objects.get(pk = id)
    except Document.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = DocumentsSerializers(data_doc)
        return Response(serialize.data)
    
    elif request.method == 'DELETE':
        data_doc.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serialize = DocumentsSerializers(data_doc, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)