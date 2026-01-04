from django.db import models

# Create your models here.
class AccessResource(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view_dashboard","Can view dashboard"),
            ("can_export_data","Can export data"),
        ]

        def __str__(self):
            return self.name
