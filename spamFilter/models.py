from django.db import models

# Create your models here.
class Ham(models.Model):
    label = models.CharField(max_length=10)
    msg = models.TextField(max_length=800)
   
    def _str_(self):
        return self.msg

class Spam(models.Model):
    label = models.CharField(max_length=10)
    msg = models.TextField(max_length=800)
   
    def _str_(self):
        return self.msg