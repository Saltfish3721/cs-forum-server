from django.db import models


class article(models.Model):

	articleID  = models.AutoField(primary_key=True)

	title      = models.CharField(max_length=32,default="title")
	content    = models.TextField(null=True)
	
	up         = models.IntegerField(default=0)
	down       = models.IntegerField(default=0)
	pageview   = models.IntegerField(default=0)
	submitDate = models.DateField(auto_now = True)
	content    = models.TextField(null=True)

	def __str__(self):
		return self.title


# class articleBody(models.Model):

# 	articleID  = models.IntegerField(primary_key=True)
# 	title      = models.CharField(max_length=32)
# 	topic      = models.CharField(max_length=32)
# 	content    = models.TextField(null=True)

# 	def __str__(self):
# 		return self.title


class users(models.Model):

	userID    = models.IntegerField(primary_key=True)
	name      = models.TextField(null=True)
	email     = models.EmailField()
	level     = models.IntegerField()
	password  = models.TextField(null=True)


	def __str__(self):
		return self.name