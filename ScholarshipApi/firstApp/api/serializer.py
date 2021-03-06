from rest_framework import serializers
from firstApp.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):
    """Serializes a Scholarship object"""

    class Meta:
        model = Scholarship
        fields = ['id', 'scholarship_name', 'scholarship_description']
