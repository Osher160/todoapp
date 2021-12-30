from django.db import models

# Create your models here.
class todoapp(models.Model):
    text=models.CharField(max_length=45)
    complited=models.BooleanField(default=False)

    def __str__(self):
        return self.text