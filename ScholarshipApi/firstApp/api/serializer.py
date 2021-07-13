from rest_framework import serializers
from firstApp.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ['scholarship_name', 'scholarship_description']
