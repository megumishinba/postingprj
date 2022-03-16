from django.db import models
from django.contrib.auth.models import User

EVALUATION_CHOICES =[('良い','良い'),('悪い','悪い')]
class PostingModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')
    useful_review = models.IntegerField(null=True, blank=True, default=0)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices=EVALUATION_CHOICES)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title
        

# Create your models here.
