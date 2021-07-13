from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ScholarshipSerializer
from firstApp.models import Scholarship


class ScholarshipViewset(viewsets.ModelViewSet):
    """Scholarship API Viewset"""
    serializer_class = ScholarshipSerializer
    queryset = Scholarship.objects.all()


class ScholarshipSearchViewset(viewsets.ModelViewSet):
    """Scholarship Search API Viewset"""
    serializer_class = ScholarshipSerializer
    queryset = Scholarship.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """Overwriting the viewset retrieve function in order to filter through database using url parameter"""
        params = kwargs
        scholarships_filter = Scholarship.objects.filter(
            scholarship_name__contains=params['pk'])
        serializer = ScholarshipSerializer(scholarships_filter, many=True)
        return Response(serializer.data)
