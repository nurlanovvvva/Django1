from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.title




