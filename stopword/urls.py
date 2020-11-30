from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.StopWordViewset)



app_name = 'stopword'

urlpatterns = [
    path('add', views.add_stopword, name='add_stopword'),
    path('', include(router.urls))
]