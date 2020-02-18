from django.db import models

# Create your models here.
class Stu(models.Model):
	id = models.IntegerField(primary_key=True,auto_created=True)
	name = models.CharField(max_length=200)