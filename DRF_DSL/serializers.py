from rest_framework import serializers
from DRF_DSL.models import University


class DRF_DSLSerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ('id',
              'name',
              )
