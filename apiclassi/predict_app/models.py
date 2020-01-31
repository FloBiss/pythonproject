from django.db import models


# Create your models here.
class Subject(models.Model):
	AGE = models.IntegerField()
	SPORT = models.IntegerField()
	WEIGHT = models.IntegerField()
	HEIGHT = models.IntegerField()
	label = models.FloatField()
	zchest = models.FloatField()
	zwrist = models.FloatField()
	temp = models.FloatField()
	
	activity = models.FloatField(null=True)
	
	def __str__(self):
		return f'un sujet age de {self.AGE} ans'
	
