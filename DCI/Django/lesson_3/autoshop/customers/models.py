from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=200, null=True)

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='vehicle'
    )

    class Meta:
        abstract = True


class Car(Vehicle):
    model_name = models.CharField(max_length=200, null=True)
    yom = models.DateField()


class Worker(models.Model):
    name = models.CharField(max_length=200, null=True)
    speciality = models.CharField(max_length=200, null=True)


class Machine(models.Model):
    name = models.CharField(max_length=200, null=True)
    workers = models.ManyToManyField(
        Worker, related_name='machine', blank=True
    )
    comm_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['machine_name', 'worker']
