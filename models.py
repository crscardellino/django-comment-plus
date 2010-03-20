import datetime

from django.db import models

from django.contrib import comments

Comment = comments.get_model()

class Karma(models.Model):
	user = models.ForeignKey('auth.User')
	comment = models.ForeignKey(Comment)
	date_added = models.DateTimeField(default=datetime.datetime.now)
	class Meta:
		unique_together = ('user','comment',)
