from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Category, Order
from .serializers import ItemSerializer, OrderSerializer
from django.db.models.query_utils import Q
from django.utils import timezone
from datetime import timedelta

# Item 기능
class ItemView(APIView):
    # Category에 따른 Item 조회
    def get(self, request):
        category = request.GET['category']
        category = Category.objects.get(name=category)

        items = Item.objects.filter(category=category)
    
        return Response(ItemSerializer(items, many=True).data)

    # Item 등록
    def post(self, request):
        print(request.data)
        item_serializer = ItemSerializer(data=request.data)

        if item_serializer.is_valid():
            item_serializer.save()
            return Response({'message': "저장 완료!!"}, status=status.HTTP_200_OK)
        
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Order 기능
class OrderView(APIView):
    # id로 Order 조회
    def get(self, request):
        order_id = request.GET['order_id']
        AWeekAgo = timezone.now() - timedelta(days=7)

        query = Q(id=order_id) & Q(order_date__gte=AWeekAgo)
        order = Order.objects.get(query)

        return Response(OrderSerializer(order).data)
