from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView

router = DefaultRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('', include(router.urls)),
]