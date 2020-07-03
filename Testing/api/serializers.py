from rest_framework import serializers

from Testing.models import DataTesting



class DataTestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTesting
        fields = ['image', 'label', 'directory']