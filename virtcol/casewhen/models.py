from django.db import models

class CaseWhen(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
