from django.urls import path
from .views import PollViewSet, ChoiceViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('polls', PollViewSet, basename='Polls')
router.register('choices', ChoiceViewSet, basename='Choices')
urlpatterns = router.urls
