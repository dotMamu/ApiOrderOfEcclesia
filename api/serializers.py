from rest_framework import serializers
from .models import GlyphUnion, Weapon



class GlyphUnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlyphUnion
        fields = '__all__'

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'