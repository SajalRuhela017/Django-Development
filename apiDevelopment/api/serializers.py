from rest_framework import serializers
from .models import tempModel

class tempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tempModel
        fields = ('title', 'description')