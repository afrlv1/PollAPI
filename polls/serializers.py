from rest_framework import serializers
from .models import Poll, Choice


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'poll',
            'description',
            'start_date',
            'finish_date',
        )
        model = Poll


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'poll',
            'question',
            'choice',
            'voted',
            'typeOfChoice',
        )
        model = Choice
