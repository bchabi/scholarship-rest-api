from django.db import models


class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=255)
    scholarship_description = models.TextField(max_length=255)

    def __str___(self):
        return self.scholarship_name
