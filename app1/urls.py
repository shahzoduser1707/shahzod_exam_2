from django.urls import path
from .views import getAllUstalar,getAllOrderlar,Orderyaratish,OrderOzgartirish,OrderniOchirish,getUstaId

urlpatterns = [
    path('getall/ustalar/', getAllUstalar.as_view()),
    path('getall/orderlar/', getAllOrderlar.as_view()),
    path('create/order/', Orderyaratish.as_view()),
    path('update/order/<int:order_id>', OrderOzgartirish.as_view()),
    path('delete/order/<int:order_id>', OrderniOchirish.as_view()),
    path('get/ustaid/<int:usta_id>',getUstaId.as_view())
]