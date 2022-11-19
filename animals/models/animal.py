from django.db import models

# Create your models here.
class Animal(models.Model):
    basic_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The {self.scientific_name}, also known as {self.basic_name}."

    def as_dict(self):
        return {
            'id': self.id,
            'basic_name': self.basic_name,
            'scientific_name': self.scientific_name,
        }