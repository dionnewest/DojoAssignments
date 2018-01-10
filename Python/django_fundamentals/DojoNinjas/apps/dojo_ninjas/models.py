from __future__ import unicode_literals

from django.db import models

# Create your models here.

class dojo(models.Model):
	name = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=2)
	def __repr__(self):
		return "dojo object: {} from {},{}".format(self.name, self.city, self.state)

class ninja(models.Model):
	dojo_id = models.ForeignKey(dojo, related_name="ninjas")
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	def __repr__(self):
		return "ninja object: {} {}, at {}".format(self.first_name, self.last_name, self.dojo_id.name)
