from django.conf.urls import url
from .views import CoordinateLoggerAPIHandler

# API endpoints
urlpatterns = [
    url(r'^coordinates$',
        CoordinateLoggerAPIHandler.as_view(),
        name='coordinates-logger'),
]
