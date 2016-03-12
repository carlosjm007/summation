# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class visitas(models.Model):
	visita = models.CharField(max_length = 45)
	class Meta:
		db_table = 'visitas'
	def __unicode__(self):
		return self.visita

class cubo(models.Model):
	cubo = models.TextField()
	tamano = models.CharField(max_length = 2)
	class Meta:
		db_table = 'cubo'
	def __unicode__(self):
		return self.id