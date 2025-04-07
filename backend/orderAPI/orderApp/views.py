from django.shortcuts import render
from orderAPI.serializer import OrderSerializer
from .models import OrderModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
# Create your views here.




class OrderApiView(APIView):

    def get(self, request):
        return Response({"message": "Use POST"})



    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(status=HTTP_400_BAD_REQUEST)
    # {"contact_bio": "some bio", "adress": "some adress"}