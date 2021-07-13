from django.db import models


class Scholarship(models.Model):
    """Create a database model for Scholarships in the system"""
    scholarship_name = models.CharField(max_length=255)
    scholarship_description = models.TextField(max_length=255)

    def __str___(self):
        """Return string representation of the scholarship name"""
        return self.scholarship_name
