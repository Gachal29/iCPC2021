from django.db import models

class Ingredients(models.Model):
  
  name = models.CharField(
    max_length=500,
    null=False,
  ) 
  
  field = models.CharField(
    blank=False,
    null=False,
    max_length=100,
    default=''
  )

  iid = models.CharField(
    primary_key=True,
    max_length=10,
    null=False
  )

  def __str__(self):
    return '<Ingredients iid=' + self.iid + 'name="' + self.name + '">'
