from django.db import models


class articleInfo(models.Model):

	title      = models.CharField(max_length=32,default="title")
	info       = models.TextField(null=True)
	articleID  = models.ForeignKey('articleBody', on_delete=models.CASCADE)
	authorID   = models.ForeignKey('users', on_delete=models.CASCADE)
	up         = models.IntegerField(default=0)
	down       = models.IntegerField(default=0)
	pageview   = models.IntegerField(default=0)
	submitDate = models.DateField(auto_now = True)

	def __str__(self):
		return self.title


class articleBody(models.Model):

	articleID  = models.IntegerField(primary_key=True)
	title      = models.CharField(max_length=32)
	topic      = models.CharField(max_length=32)
	content    = models.TextField(null=True)

	def __str__(self):
		return self.title


class users(models.Model):

	userID    = models.IntegerField(primary_key=True)
	name      = models.TextField(null=True)
	email     = models.EmailField()
	level     = models.IntegerField()
	password  = models.TextField(null=True)


	def __str__(self):
		return self.name