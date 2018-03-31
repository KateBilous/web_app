from django.db import models

# Create your models here.

class Document(models.Model):

    name= models.CharField(max_length=255)
    text= models.TextField()

    def __str__(self):
        return self.name


# class Comment(models.Model):
#     '''комментарий  - это некоторый текст, относящийся  к данному документу'''
#     document = models.ForeignKey(Document, related_name='comments')
#     text = models.TextField()
