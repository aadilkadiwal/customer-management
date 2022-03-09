from django.db import models

class Abstract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True