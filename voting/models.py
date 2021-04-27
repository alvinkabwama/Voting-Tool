from django.db import models
  
# Create your models here.
class Vote(models.Model):
    
    id_number = models.AutoField(primary_key=True)
    rotary_number = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    president_vote = models.CharField(max_length = 255)
    secretary_vote = models.CharField(max_length = 255)
       
    def __str__(self):
        '''Return a string representation of the model.'''
        return self.rotary_number