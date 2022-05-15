from django.db import models
from django.urls import reverse
# Create your models here.


class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])
