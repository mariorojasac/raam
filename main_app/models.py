from django.db import models
from django.urls import reverse
from datetime import date

SERVICES = (
    ('P', 'Pick Up'),
    ('D', 'Drop Off'),
)


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name






class Pantry(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.TextField(max_length=250)
    foods = models.ManyToManyField(Food)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})



    


class Schedule(models.Model):
    service = models.CharField(
        max_length=1,
        choices= SERVICES,
        default=SERVICES[0][0],
    )
    date = models.DateField('Schedule Date')

    pantry = models.ForeignKey(Pantry, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_service_display()} on {self.date}'

    class Meta:
        ordering = ['-date']