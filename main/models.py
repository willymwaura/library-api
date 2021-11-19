from django.db import models
from django .utils import timezone

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Textbook(models.Model):
    name=models.CharField(max_length=100)
    booktype=models.ForeignKey(Category,related_name='Textbook',on_delete=models.CASCADE)
    price=models.IntegerField(default=400)
    pages=models.IntegerField(default=400)
    date_created=models.DateField(default=timezone.now())
   
    
    def __str__(self):
        return '{}{}'.format(self.name,self.price)
    


class Novels(models.Model):
    name=models.CharField(max_length=100)
    novelcategory=models.ForeignKey(Category,related_name='Novels',on_delete=models.CASCADE)
    price=models.IntegerField(default=400)
    pages=models.IntegerField(default=500)
    date_created=models.DateField(default=timezone.now())
    
    
    def __str__(self):
        return '{}{}'.format(self.name,self.price)
    


