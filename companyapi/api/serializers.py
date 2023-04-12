from rest_framework import serializers
from api.models import Company

#Create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
