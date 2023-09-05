from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Clanak(models.Model):
    naslov = models.CharField(max_length=100)
    sadrzaj = models.TextField()
    datum_objave = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.naslov
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})
    