from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    software = models.ManyToManyField('Software')
    date = models.DateTimeField(auto_now_add=True)
    overview = models.TextField(max_length=1000)

    def __str__(self):
        return self.title




class Software(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
