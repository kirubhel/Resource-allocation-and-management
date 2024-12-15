# inventory/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        """ Get all items for a specific category """
        category = self.get_object()
        items = Item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

# Item ViewSet
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['put'])
    def update_reorder_point(self, request, pk=None):
        """ Business logic to update reorder point """
        item = self.get_object()
        reorder_point = request.data.get("reorder_point")
        if reorder_point is not None:
            item.reorder_point = reorder_point
            item.save()
            return Response({'status': 'Reorder point updated'})
        return Response({'error': 'Reorder point is required'}, status=400)
