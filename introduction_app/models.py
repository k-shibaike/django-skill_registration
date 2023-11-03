from django.db import models
from django.urls import reverse


class Skill(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images', null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )

  def get_absolute_url(self):
        return reverse('introduction_app:index')

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images', null=True)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )

  def get_absolute_url(self):
        return reverse('introduction_app:index')

  def __str__(self):
    return self.name


