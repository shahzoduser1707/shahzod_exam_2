from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ustalar,Orderlar
from .serializer import UstalarSerializer,OrderlarSerializer


class getAllUstalar(APIView):
    def get(self,request):
        a = Ustalar.objects.all()
        serializer = UstalarSerializer(a, many = True)
        return Response(serializer.data)
    
class getAllOrderlar(APIView):
    def get(self,request):
        b = Orderlar.objects.all()
        serializer = OrderlarSerializer(b,many = True)
        return Response(serializer.data)
    
class Orderyaratish(APIView):
    def post(self,request):
        serializer = OrderlarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

class OrderOzgartirish(APIView):
    def patch(self,request,*args,**kwargs):
        c = get_object_or_404(Orderlar , id = kwargs['order_id'])
        serializer = OrderlarSerializer(c,data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)   
class OrderniOchirish(APIView):
    def delete(self,request,*args,**kwargs):
        d = get_object_or_404(Orderlar, id = kwargs['order_id'])
        d.delete()
        return Response({"id which you chose":"successfully deleted"})
    
class getUstaId(APIView):
    def get(self,request,*args,**kwargs):
        e = Orderlar.objects.filter(Ustalar = kwargs['usta_id'])
        serializer = OrderlarSerializer(e, many = True)
        return Response(serializer.data)