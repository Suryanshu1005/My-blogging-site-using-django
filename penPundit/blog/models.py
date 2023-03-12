from django.db import models

# Create your models here.

# we will create our category model here

class Category(models.Model):
    title = models.CharField(max_length=100)
    cat_id = models.AutoField(primary_key=True)
    description = models.TextField()
    url=models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


#Post models will be created here

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat= models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')


    #always run python manage.py makemigrations and migrate
    #to implement all the changes made to models.