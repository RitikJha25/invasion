from django.db import models
from django.contrib.auth.models import User


CHOICES_FIELD = {
	('true', 'True'),
	('false', 'False'),
}
# Create your models here.
class MakeBlogs(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE,unique = False, related_name = "makeblogs", null = True)
	date = models.DateField(auto_now_add = True)
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 100000000)
	reference = models.CharField(max_length = 1000)
	image = models.ImageField(upload_to = 'gallery/')
	likes = models.ManyToManyField(User, related_name = "likes", blank = True)
	dislikes = models.ManyToManyField(User, related_name = "dislikes", blank = True)
	saveduser = models.ManyToManyField(User, related_name = "saveduser", blank = True)


	def __str__(self):
		return self.title
		return self.description
		return self.reference



	@property
	def num_likes(self):
		return self.likes.all.count()
		return self.dislikes.all.count()

class Comments(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE,unique = False, null = True)
	post = models.ForeignKey(MakeBlogs, on_delete = models.CASCADE)
	commentor =  models.ManyToManyField(User, related_name = "commentor", blank = True)
	comment = models.CharField(max_length = 1000,)
	comment_date = models.DateTimeField(auto_now_add  =True )
