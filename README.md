# Scholarship Django REST API


1. This is a python [Django](https://www.djangoproject.com/) project that uses the [Django Rest Framework](https://www.django-rest-framework.org/) and has an API with the following two endpoints:
  1. `api/scholarships` which returns a list of scholarships
  1. `api/search/<search_term>` which returns a subset of scholarships matching the search term

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install django
pip install djangorestframework
```

## Usage

Use software such as Postman to test the outputs of the API

```python
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

```

## License
[MIT](https://choosealicense.com/licenses/mit/)