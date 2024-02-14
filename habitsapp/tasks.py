from datetime import datetime, timezone, timedelta
import os
import telebot
from celery import shared_task
from habitsapp.models import Habit

API_KEY = os.getenv('TELEGRAM_BOT_API_KEY')


@shared_task
def reminder_habits():
    now = datetime.now(tz=timezone.utc)

    bot = telebot.TeleBot(API_KEY)

    habits = Habit.objects.filter(time__lte=now)
    print(habits)

    for habit in habits:
        chat_id = habit.user.telegram_id
        print(chat_id)
        message = f"Привет {habit.user}! Время {habit.time}. Пора идти в {habit.place} и сделать {habit.action}." \
                  f"Это займет {habit.duration} минут!"

        try:
            response = bot.send_message(chat_id=chat_id, text=message)
            print(response)

            for i in range(7):
                day = i + 1
                if habit.period == day:
                    habit.time += timedelta(days=day)
                    break

        except Exception as e:
            print(e)

        finally:
            habit.save()
