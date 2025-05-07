from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Settlement
from .serializers import SettlementSerializer

class SettlementCollectionView(APIView):
    def get(self, request):
        settlements = Settlement.objects.all()
        serializer = SettlementSerializer(settlements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SettlementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SettlementItemView(APIView):
    def get_object(self, pk):
        try:
            return Settlement.objects.get(pk=pk)
        except Settlement.DoesNotExist:
            return None

    def get(self, request, pk):
        settlement = self.get_object(pk)
        if not settlement:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SettlementSerializer(settlement)
        return Response(serializer.data)

    def put(self, request, pk):
        settlement = self.get_object(pk)
        if not settlement:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SettlementSerializer(settlement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        settlement = self.get_object(pk)
        if not settlement:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        settlement.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
