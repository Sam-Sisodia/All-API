'''
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
        serializer = productserializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)

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

    def delete(seif,request,id=None,format=None):
        productid = get_object_or_404(Products,id=id)
        productid.delete()
        return Response({'msg':"Delete Successfully"},status=status.HTTP_200_OK)


             return Response(status=status.HTTP_400_BAD_REQUEST)

'''