from rest_framework.serializers import ModelSerializer
from .models import StopWord

class StopWordSerializer(ModelSerializer):

    class Meta:
        model = StopWord
        fields = '__all__'