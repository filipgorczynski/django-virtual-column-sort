from rest_framework import serializers

from .models import CaseWhen


class CaseWhenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaseWhen
        fields = ('name',)
