from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Courier
from .serializers import CourierSerializer


class CourierCollectionView(APIView):
    def get(self, request):
        couriers = Courier.objects.all()
        serializer = CourierSerializer(couriers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourierItemView(APIView):
    def get_object(self, pk):
        try:
            return Courier.objects.get(pk=pk)
        except Courier.DoesNotExist:
            return None

    def get(self, request, pk):
        courier = self.get_object(pk)
        if not courier:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourierSerializer(courier)
        return Response(serializer.data)

    def put(self, request, pk):
        courier = self.get_object(pk)
        if not courier:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourierSerializer(courier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        courier = self.get_object(pk)
        if not courier:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        courier.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
