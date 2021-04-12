from django.db import models

class Tasks(models.Model):

    TO_DO= models.CharField(max_length=200)
    complete= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TO_DO

