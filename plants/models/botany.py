from django.db import models

# Create your models here.
class Botany(models.Model):
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.short_desc}."

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'short_desc': self.short_desc,
        }