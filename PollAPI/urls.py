from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('api/v1/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
