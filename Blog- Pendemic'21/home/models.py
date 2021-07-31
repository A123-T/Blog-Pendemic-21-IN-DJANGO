from django.db import models

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 13)
    query = models.TextField(max_length = 255)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return 'Message from ' + self.email

    

   


