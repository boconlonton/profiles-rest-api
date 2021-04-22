from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP method as function (get,post,patch,put,delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'HellO',
                         'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # Instantiate the HelloSerializer class
        serializer = self.serializer_class(data=request.data)

        # Invoke the built-in validation process of serializer class
        if serializer.is_valid():
            # Retrieve the 'name' from the validated data
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            # Default, Response object status_code = 200
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,  # self-generated error dictionary of serializer class
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
