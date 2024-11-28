from django.db import models

from django.db import models
from django.utils.text import slugify

class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    pic = models.FileField(upload_to='questions/pictures')
    slug = models.SlugField(unique=True, blank=True)  # Unique slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    answer = models.TextField()
    file = models.FileField(upload_to='answers/')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['question']