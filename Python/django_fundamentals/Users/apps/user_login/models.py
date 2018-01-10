from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email_address = models.CharField(max_length=50)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<user object: {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email_address)