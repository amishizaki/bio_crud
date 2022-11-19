from django.db import models
from .field import Field

# Create your models here.
class Plant(models.Model):
    basic_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name='field_of_study'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The {self.scientific_name}, also known as {self.basic_name}. Botany branch: {self.field}"

    def as_dict(self):
        return {
            'id': self.id,
            'basic_name': self.basic_name,
            'scientific_name': self.scientific_name,
            'field': self.field,
        }