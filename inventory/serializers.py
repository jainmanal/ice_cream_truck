from rest_framework import serializers
from .models import IceCream, ShavedIce, SnackBar

class IceCreamSerializer(serializers.ModelSerializer):

    class Meta:
        model = IceCream
        exclude = ('sold',)

class ShavedIceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShavedIce
        exclude = ('sold',)

class SnackBarSerializer(serializers.ModelSerializer):

    class Meta:
        model = SnackBar
        exclude = ('sold',)