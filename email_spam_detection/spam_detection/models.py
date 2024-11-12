# spam_detection/models.py

from django.db import models

class EmailSubmission(models.Model):
    email = models.TextField()
    is_spam = models.BooleanField(default=False)
