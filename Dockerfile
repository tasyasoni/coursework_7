FROM python:3

WORKDIR /Habits_tracker_Docker

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .