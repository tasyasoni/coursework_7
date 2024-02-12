from django.urls import path

from habitsapp.apps import HabitsappConfig
from habitsapp.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitsappConfig.name

urlpatterns = [
    path('habit_list/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit_update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_change'),
    path('habit_delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete')
]
