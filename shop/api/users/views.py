from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from api.users.serializers import RegisterSerializer, LoginSerializer, LogoutSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
            username=serializer.validated_data["username"],
        )
        user.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request=request,
            password=serializer.validated_data["password"],
            username=serializer.validated_data["username"],
        )
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        token = Token.objects.get_or_create(user=user)[0].key
        return Response(
            status=status.HTTP_200_OK, data={"user_id": user.id, "token": token}
        )


class LogoutView(CreateAPIView):
    serializer_class = LogoutSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # request.auth.delete()
        user = authenticate(request=request, token=serializer.validated_data["token"])
        user._logged_out.send(
            sender=request.user.__class__, request=request, user=request.user
        )
        return Response(
            data=serializer.validated_data, status=status.HTTP_204_NO_CONTENT
        )
