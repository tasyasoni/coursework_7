from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from usersapp.models import User
from usersapp.serializers import UserSerializer
from habitsapp.permissions import IsOwner


class UserRegisterAPIView(generics.CreateAPIView):
    """Класс для создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    """ Класс для вывода списка пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс для вывода одного пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Класс для изменения пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Класс для удаления пользователя """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
