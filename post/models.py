import random
import string
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    name = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=50)
    post_url = models.CharField(max_length=15, blank=True)
    expiry_date = models.DateField(null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def random_string(self, length):
        return ''.join(random.choice(string.ascii_letters) for l in range(length))


@receiver(pre_save, sender=Post)
def generate_slug(sender, instance, *args, **kargs):
    # Check for all expired posts and delete them
    # In a real application you'll do this using Celery and Rabitmq
    # Or write a cutome command and execute it from a cron-tab or airflow
    if len(Post.objects.all()) > 1:
        for post in Post.objects.all():
            if datetime.date(datetime.today()) > post.expiry_date:
                post.delete()
    if instance.name:
        instance.slug = slugify(instance.name)
        instance.post_url = instance.random_string(7)
