from rest_framework.viewsets import ModelViewSet

from .models import StopWord
from .serializers import StopWordSerializer

class StopWordViewset(ModelViewSet):
    
    queryset = StopWord.objects.all().order_by('-id')
    serializer_class = StopWordSerializer