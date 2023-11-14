from rest_framework import serializers

from time_location.models import Time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'