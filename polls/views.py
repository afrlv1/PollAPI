from rest_framework import viewsets
from . import models
from . import serializers


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
