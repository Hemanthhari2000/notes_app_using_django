from django.db import models

# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


# def user_profile(sender, instance, created, **kwargs):
#     if created:
#         Note.objects.create(user=instance)
#         print("Profile Created!")


# post_save.connect(user_profile, sender=User)
