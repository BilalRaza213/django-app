from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    passport_details = models.CharField(max_length=100)
    manager = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True
    )


class Event(models.Model):
    event_type_choices = [
        ("wedding", "Wedding"),
        ("birthday", "Birthday"),
        ("themed_party", "Themed Party"),
        ("graduation", "Graduation"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    location = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=20, choices=event_type_choices)
    theme = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    duration = models.TimeField()
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE, null=True, default='')
    caterer = models.ForeignKey("Caterer", on_delete=models.CASCADE, null=True, default='')
    client = models.ForeignKey("Client", on_delete=models.CASCADE, null=True, default='')
    guests = models.ManyToManyField("Guest", related_name='events')
    
    def __str__(self):
        return self.title



class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)


class Guest(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    min_guests = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()


class Caterer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=100)
    menu = models.TextField()
    min_guests = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()
