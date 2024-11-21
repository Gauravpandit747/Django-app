from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# @api_view(['POST'])
# def api_home(request, *args, **kwargs) :
#     # print(request.headers)
#     # print(request.content_type)
#     # return JsonResponse({"data":"success"})

#     instance  =  Product.objects.all().order_by('?').first()
#     data = {}
#     data1 = request.data
#     if instance:
#         # data['id'] = instance.id
#         # data['title'] = instance.title
#         # data['content'] = instance.content
#         # data['price'] = instance.price

#     # model to dict method 
#     #     data = model_to_dict(instance, fields=['id', 'title', 'sale_price'])
#     # return Response(data)

#     # using serializers 
#         data = ProductSerializer(instance).data
#         return Response(data1)


# Serializing the post data from the request:  
@api_view(['POST'])
def api_home(request, *args, **kwargs) :
    data = request.data
    # using serializers 
    serializer  = ProductSerializer(data = request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        print(":::::::::::::::::::::")
        print(serializer.data)
        print(":::::::::::::::::::::")
        # data = serializer.data
        return Response(serializer.data)

