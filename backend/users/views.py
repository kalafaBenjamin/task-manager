from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LoginSerializer, RegisterSerializer


class LoginView(APIView):

    authentication_classes = []

    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response(
            serializer.validated_data
        )
    
class RegisterView(APIView):

    authentication_classes = []

    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {"message": "User created"}
        )