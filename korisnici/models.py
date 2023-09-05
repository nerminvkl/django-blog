from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slika = models.ImageField(default='default.jpg', upload_to='profilne_slike')

    def __str__(self):
        return f'{self.user.username} profil'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.slika.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.slika.path)