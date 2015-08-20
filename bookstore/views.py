from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookstore.models import Books, Prices, Authors
from bookstore.serializers import BooksSerializer, PricesSerializer
from ratelimit.decorators import ratelimit

# Create your views here.
@ratelimit(key='ip', rate='10/m', block=True, method=['GET', 'POST'])
@api_view(['GET', 'POST',])
def getBooksAndAddBooks(request):
    if request.method == 'GET':
        queryset = Books.objects.all()
        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@ratelimit(key='ip', rate='10/m', block=True, method=['GET', 'PUT'])
@api_view(['GET', 'PUT',])
# @renderer_classes((TemplateHTMLRenderer,))
def book_detail(request, pk):
     try:
        book = Books.objects.get(pk=pk)
     except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)

     elif request.method == 'PUT':
        serializer = BooksSerializer.create(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)