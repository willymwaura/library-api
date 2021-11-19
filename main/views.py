
from django.shortcuts import render
from django.http import HttpResponse, request, response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.views import Response
from main.models import Category,Novels,Textbook
from main.serializer import Novelsserializer, Textbookserializer

# Create your views here.
class alltextbooklist(APIView):
    def get(self,request):
        books=Textbook.objects.all()
        serializer=Textbookserializer(books,many=True)
        return Response (serializer.data)

    def post(self,request):
        serializer=Textbookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)

class allnovellist(APIView):
    def get(self,request):
        books=Novels.objects.all()
        serializer=Novelsserializer(books,many=True)
        return Response (serializer.data)

    def post(self,request,pk):
        serializer=Novelsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
class deletetext(APIView):
    def delete(Self,request,pk):
        book=Textbook.objects.get(id=pk)
        book.delete()
        return Response("deleted")
class deletenovels(APIView):
    def delete(Self,request,pk):
        book=Novels.objects.get(id=pk)
        book.delete()
        return Response('Deleted')



