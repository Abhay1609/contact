from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import *


class ContactView(APIView):
    def get(self,request):
        allBooks=contact_form.objects.all().values()
        return Response({"Message":"List of member","Member":allBooks})
    def post(self,request):
        contact_form.objects.create(name=request.data["name"],
                                    surname=request.data["surname"],
                                    phone=request.data["phone"],
                                    email=request.data["email"],
                                    message=request.data["message"],)
        Books=contact_form.objects.all().filter(name=request.data["name"]).values()
        return Response({"Message":"new message","Book":Books})