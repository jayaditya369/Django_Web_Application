from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models import ManyToManyField
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField(default=12)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
            MaxValueValidator(500),
            MinValueValidator(50)
        ])
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    num_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Student(User):
    LVL_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('ND', 'No Degree'),
    ]

    level = models.CharField(choices=LVL_CHOICES, max_length=2, default='HS')
    address = models.CharField(max_length=300, blank=True)
    province = models.CharField(max_length=2, default='ON')
    registered_courses = models.ManyToManyField(Course, blank=True)
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return self.first_name+' '+self.last_name


class Order(models.Model):
    courses = models.ManyToManyField(Course)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    order_status_choices = [
        (0, 'Cancelled'),
        (1, 'Confirmed'),
        (2, 'On Hold')
    ]
    order_status = models.IntegerField(choices=order_status_choices, default=1)
    order_date = models.DateField(default=timezone.now())

    def total_items(self):
        total_items = 0
        for i in self.courses.all():
            total_items = total_items + 1
        return str(total_items)

    def total_cost(self):
        total_price = 0
        for i in self.courses.values('price'):
            total_price = total_price + i['price']
        return str(total_price)

    def __str__(self):
        return Student.__str__(self.student) + ' Order of total cost : ' + self.total_cost()


class Review(models.Model):
    reviewer = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comments = models.TextField(blank= True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.reviewer

