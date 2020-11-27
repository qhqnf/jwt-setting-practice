from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StopWordViewset

router = DefaultRouter()
router.register('', StopWordViewset)



app_name = 'stopword'

urlpatterns = [
    path('', include(router.urls))
]