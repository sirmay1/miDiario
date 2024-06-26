from django.db import models


class Diario(models.Model):
    user = models.CharField(max_length=100)
    topic = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, max_length=800)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.user + '|' + self.topic + '|' +  self.description + '|' + str(self.start_date) + '|' + str(self.completed)

# Create your models here.








