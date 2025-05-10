from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Return
from .serializers import ReturnSerializer


class ReturnCollectionView(APIView):
    def get(self, request):
        returns = Return.objects.all()
        serializer = ReturnSerializer(returns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReturnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnItemView(APIView):
    def get_object(self, pk):
        try:
            return Return.objects.get(pk=pk)
        except Return.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReturnSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReturnSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
