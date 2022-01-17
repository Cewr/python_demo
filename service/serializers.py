from rest_framework import serializers

from . models import Chess


class Slll(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Chess
