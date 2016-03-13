# -*- encoding: utf-8 -*-
from django.db import models

class cubo(models.Model):
	cubo = models.TextField()
	tamano = models.CharField(max_length = 2)
	class Meta:
		db_table = 'cubo'
	def __unicode__(self):
		return self.id