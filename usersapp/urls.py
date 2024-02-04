from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usersapp.apps import UsersappConfig

from usersapp.views import UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UsersRegistrationView

app_name = UsersappConfig.name


urlpatterns = [
    path('user/list/', UserListAPIView.as_view(), name='user_list'),
    path('user/register/', UsersRegistrationView.as_view(), name='register'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_one'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]