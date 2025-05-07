from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fulfilment
from .serializers import FulfilmentSerializer

class FulfilmentCollectionView(APIView):
    def get(self, request):
        fulfilments = Fulfilment.objects.all()
        serializer = FulfilmentSerializer(fulfilments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FulfilmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FulfilmentItemView(APIView):
    def get_object(self, pk):
        try:
            return Fulfilment.objects.get(pk=pk)
        except Fulfilment.DoesNotExist:
            return None

    def get(self, request, pk):
        fulfilment = self.get_object(pk)
        if not fulfilment:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FulfilmentSerializer(fulfilment)
        return Response(serializer.data)

    def put(self, request, pk):
        fulfilment = self.get_object(pk)
        if not fulfilment:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FulfilmentSerializer(fulfilment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fulfilment = self.get_object(pk)
        if not fulfilment:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        fulfilment.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
