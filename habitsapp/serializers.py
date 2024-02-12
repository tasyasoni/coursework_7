from rest_framework import serializers

from habitsapp.models import Habit
from habitsapp.validators import validator_for_habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Привычки """

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            validator_for_habit,
        ]
