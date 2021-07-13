from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ScholarshipSearchViewset, ScholarshipViewset


router = DefaultRouter()
router.register('scholarship', ScholarshipViewset, basename='scholarship')
router.register('scholarship/search',
                ScholarshipSearchViewset, basename='search')

urlpatterns = [
    url('', include(router.urls)),
]
