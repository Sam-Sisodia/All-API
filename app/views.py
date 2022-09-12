#from urllib import request

from ast import Delete
from functools import partial
from urllib import request
from venv import create
from django.shortcuts import render
from . models import *
from . serializer import *
from  rest_framework import serializers
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets


from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin ,CreateModelMixin, UpdateModelMixin, DestroyModelMixin,RetrieveModelMixin



# Create your views here.


def home(request):
    return render(request , "wel.html")

'''
#Function based API =======================================================================
@api_view(['GET','POST'])
def Pruduct_list_or_create(request):
    if  request.method == "GET":
        products = Products.objects.all()
        serializer = productserializer(products,many=True)
        return Response(serializer.data , status= status.HTTP_200_OK)

    else:
        products = productserializer(data=request.data)
        if products.is_valid():
            products.save()
            return Response( products.data , status=status.HTTP_201_CREATED)
        else:
             return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def Pruduct_get_put_delete(request,id):
    if  request.method == "GET":
        products = Products.objects.get(id=id)
        serializer = productserializer(products)
        return Response(serializer.data , status= status.HTTP_200_OK)

    if  request.method == "PUT":
        products = Products.objects.get(id=id)
        serializer = productserializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status=status.HTTP_201_CREATED)
        else:
            pass

    if  request.method == "PATCH":
        products = Products.objects.get(id=id)
        serializer = productserializer(products,data=request.data , partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status=status.HTTP_201_CREATED)
        else:
            pass
          
    if  request.method == "DELETE":
        product = Products.objects.get(id=id)
        product.delete()
        return Response({'msg':"Delete Successfully"},status=status.HTTP_200_OK)

   


'''
#class Based API ============================================================

class ProductsclassAPI(APIView):
    def get(seif,request,id=None,format=None):
        if id :
            productid = get_object_or_404(Products,id=id)
            serializer = productserializer(productid)
            return Response(serializer.data , status= status.HTTP_200_OK)

        else:
            products = Products.objects.all()
            serializer = productserializer(products,many=True)
            return Response(serializer.data ,status= status.HTTP_200_OK)

    def post(seif,request,format=None):
        serializer = productserializer( data=request.data)
        print("Request .data ==========================================")
        print(request.data)
        print(type(request.data))

        print("=====================================")
        print("serilizser ========================")
        print(serializer)
        print(type(serializer))


        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(seif,request,id=None,format=None):
        productid = get_object_or_404(Products,id=id)
        serializer = productserializer(productid,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(seif,request,id=None,format=None):
        productid = get_object_or_404(Products,id=id)
        serializer = productserializer(productid,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status= status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(seif,request,id=None,format=None):
        productid = get_object_or_404(Products,id=id)
        productid.delete()
        return Response({'msg':"Delete Successfully"},status=status.HTTP_200_OK)



'''

#Generic Class-based API ==================================================


class genericAPI_list_create(generics.ListAPIView , generics.CreateAPIView):
     queryset = Products.objects.all ()
     serializer_class = productserializer



class genericAPI_update_delete(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = productserializer
    lookup_field = 'id'


    
#Generic API Mixins  ===========================================================================



class GenMixAPI_list_create(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Products.objects.all()
    serializer_class = productserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)



class GenMixAPI_update_put_delete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    
    queryset = Products.objects.all()
    serializer_class = productserializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)


    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


    



#view set =================================




class ProductsViewsetAPI(viewsets.ViewSet):
    def list(seif,request):
        products = Products.objects.all()
        serializer = productserializer(products,many=True)
        return Response(serializer.data ,status= status.HTTP_200_OK)

    def create(seif,request):
        serializer = productserializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def upadte(seif,request,id=None,format=None):
        productid = get_object_or_404(Products,id=id)
        serializer = productserializer(productid,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(seif,request,id=None,format=None):
        productid = get_object_or_404(Products,id=id)
        productid.delete()
        return Response({'msg':"Delete Successfully"},status=status.HTTP_200_OK)


'''    




    


        



    
    


        


    

    















    


