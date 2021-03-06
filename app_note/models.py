from django.db import models

from django.contrib.auth.models import User

# Create your models here.


# class Note(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=800)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.title)


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.cust_name


class Note(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    note_title = models.CharField(max_length=200, null=True)
    note_body = models.TextField(null=True)

    def __str__(self):
        return self.note_title
