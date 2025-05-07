from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Delivery
from .serializers import DeliverySerializer

class DeliveryCollectionView(APIView):
    def get(self, request):
        deliveries = Delivery.objects.all()
        serializer = DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryItemView(APIView):
    def get_object(self, pk):
        try:
            return Delivery.objects.get(pk=pk)
        except Delivery.DoesNotExist:
            return None

    def get(self, request, pk):
        delivery = self.get_object(pk)
        if not delivery:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)

    def put(self, request, pk):
        delivery = self.get_object(pk)
        if not delivery:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DeliverySerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delivery = self.get_object(pk)
        if not delivery:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        delivery.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
