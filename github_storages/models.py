from django.db import models	

class ImageInfo(models.Model):
	image_url = models.CharField(max_length=500)
	sha = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.image_url} | {self.sha}"