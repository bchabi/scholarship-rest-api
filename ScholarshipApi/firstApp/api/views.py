from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import serializers, viewsets
from .serializer import ScholarshipSerializer
from firstApp.models import Scholarship


@api_view()
def firstFunction(request):
    print(request.query_params)
    return Response({'message': 'we recieved your request'})


class ScholarshipViewset(viewsets.ModelViewSet):
    serializer_class = ScholarshipSerializer

    queryset = scholarships = Scholarship.objects.all()

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        scholarships_filter = Scholarship.objects.filter(
            scholarship_name=params['pk'])
        serializer = ScholarshipSerializer(scholarships_filter, many=True)
        return Response(serializer.data)
