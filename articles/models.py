from django.db import models

# Create your models here.


class Articles(models.Model):
    tittle=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print("***********",self.tittle)
        return self.tittle

    def snippet(self):
        return self.body[:50]+'...'
