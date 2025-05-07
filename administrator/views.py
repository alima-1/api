from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Administrator
from .serializers import AdministratorSerializer

class AdministratorCollectionView(APIView):
    def get(self, request):
        admins = Administrator.objects.all()#vending machine, panel, button.
        serializer = AdministratorSerializer(admins, many=True)#I’m giving you a list of objects, not just one — so handle them all.
        return Response(serializer.data)

    def post(self, request):
        serializer = AdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdministratorItemView(APIView):
    def get_object(self, pk):
        try:
            return Administrator.objects.get(pk=pk)
        except Administrator.DoesNotExist:
            return None
    
    # uses the get_object method to retrieve a single object based on the primary key (pk) provided in the URL.
    # This method is called when a GET request is made to the URL with a specific pk.   
    def get(self, request, pk):
        admin = self.get_object(pk)
        if not admin:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdministratorSerializer(admin)
        return Response(serializer.data)

    def put(self, request, pk):
        admin = self.get_object(pk)
        if not admin:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdministratorSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        admin = self.get_object(pk)
        if not admin:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        admin.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)





