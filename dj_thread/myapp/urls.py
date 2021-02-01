from django.urls import path
from .views import index, upload1, upload2

urlpatterns = [
    path('', index, name='index'),
    path('upload/non-threading/', upload1, name='non_thread'),
    path('upload/with-threading/', upload2, name='with_thread'),
]