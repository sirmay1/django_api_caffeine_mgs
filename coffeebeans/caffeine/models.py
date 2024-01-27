from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length= 100)
    size = models.CharField(max_length= 100)
    cup_size = models.CharField(max_length=100)
    espresso = models.CharField(max_length=100)
    total_mgs = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} | {self.size} | {self.cup_size} | {self.espresso} | {self.total_mgs}"




