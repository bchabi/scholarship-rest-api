from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ScholarshipSerializer
from firstApp.models import Scholarship


class ScholarshipViewset(viewsets.ModelViewSet):
    serializer_class = ScholarshipSerializer
    queryset = scholarships = Scholarship.objects.all()


class ScholarshipSearchViewset(viewsets.ModelViewSet):
    serializer_class = ScholarshipSerializer
    queryset = scholarships = Scholarship.objects.all()

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        scholarships_filter = Scholarship.objects.filter(
            scholarship_name__contains=params['pk'])
        serializer = ScholarshipSerializer(scholarships_filter, many=True)
        return Response(serializer.data)
