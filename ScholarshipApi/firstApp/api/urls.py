from django.conf.urls import url, include
from .views import firstFunction
from rest_framework.routers import DefaultRouter
from .views import ScholarshipViewset


router = DefaultRouter()
router.register('scholarship', ScholarshipViewset, basename='scholarship')

urlpatterns = [
    url('first', firstFunction),
    url('', include(router.urls))
]

# Need to use router for viewsets
