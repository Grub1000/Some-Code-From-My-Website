from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.utils import timezone
import math


# Create your models here.
# class Post(models.Model):
    
class post(models.Model):
    content = models.TextField()
    image = models.ImageField(default='post_default.png', upload_to='post_img')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    users_whomst_liked = models.ManyToManyField(User, related_name='likers')
    def __str__(self):
        return self.content
    def postHasMountedTime(self):
        currentTime = timezone.now()
        difference = currentTime - self.date_posted
        if difference.days == 0 and difference.seconds >= 0 and difference.seconds < 60:
            return str(difference.seconds) + 's'
        if difference.days == 0 and difference.seconds >= 60 and difference.seconds < 3600:
            return str(math.floor(difference.seconds / 60)) + 'm'
        if difference.days == 0 and difference.seconds >= 3600 and difference.seconds < 86400:
            return str(math.floor(difference.seconds / 3600)) + 'h'
        if difference.days >= 1 and difference.days < 30:
            return str(difference.days) + 'd'
        if difference.days >= 30 and difference.days < 365:
            return str(math.floor(difference.days / 30)) + ' mo.'
        if difference.days >= 365:
            return str(math.floor(difference.days / 365)) + ' y'    
class like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    liked_post = models.ForeignKey(post, on_delete=models.DO_NOTHING)
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_default.jpg', upload_to='prof_img')


    # def save(self, *args, **kwargs):
    #     super(profile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 60 or img.width > 60:
    #         output_size = (60, 60)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
            

        