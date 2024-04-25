from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializer import *
# Create your views here.

class BookApi(APIView):
    def get(self,request):
        booksdata = Book.objects.all()
        bookser = BookSerializer(booksdata,many=True)
        return Response({"data":bookser.data})
    
    def post(self,request):

        ser_data =  BookSerializer(data=request.data)
       
        if not ser_data.is_valid():
          return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"Book inserted"})


    def put(self,request):
        try:
            book_data = Book.objects.get(id=request.data['id'])
            ser_data = BookSerializer(book_data,request.data)
            if not ser_data.is_valid():
                return Response({"message":"something went wrong","errors":ser_data.errors})
            ser_data.save()
            return Response({"userdata":ser_data.data,"message":"Book Updated"})
        except Exception as e:
            return Response({"Error":"Id not found"})
        

    def delete(self,request):
        try:
            book_data = Book.objects.get(id=request.data['id'])
            book_data.delete()
            return Response({"message":"book deleted"})
        except Exception as e:
            return Response({"Error":"Id not found"})
    