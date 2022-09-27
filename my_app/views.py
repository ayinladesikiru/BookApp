from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .filter import BookFilter
from .models import Book
from .pagination import BookPagination
from .serializer import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'isbn']
    ordering_fields = ['title', 'price']
    ordering = ['title']
    pagination_class = BookPagination


class BookList(ListCreateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    # def get(self, request):
    #     queryset = Book.objects.all()
    #     serializer = BookSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class BookDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # def get(self, request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def patch(self, request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(book, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     book.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    name = "Asa"
    return render(request, "my_app/index.html", context={'name': name})


def redirect(request):
    return HttpResponseRedirect(reverse('my_app:index'))

#
