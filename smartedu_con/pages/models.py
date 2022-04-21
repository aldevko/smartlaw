from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email