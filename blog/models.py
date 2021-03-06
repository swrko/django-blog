from django.db import models
import uuid


# Create your models here.
class Blog(models.Model):
    headline = models.CharField(
        max_length=200,
        null=False,
        blank=True,
    )
    body = models.TextField(
        null=False,  # null v databaze
        blank=True,  # dovolim prazdne policko vo formulari
    )
    date = models.DateField(
        null=False,
        auto_now_add=True,  # doplni datum upravy
    )
    hidden = models.BooleanField(
        null=False,
        blank=True,
        default=True,  # moze byt callable -> volatelna funkcia
    )
    control_requested = models.BooleanField(
        null=False,
        blank=True,
        default=False,
    )

    def __str__(self):
        return self.headline


class Author(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    surname = models.CharField(
        # verbose_name="Fuckin last name",
        max_length=30,
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
    )
    blogs = models.ManyToManyField(
        to=Blog,
        related_name="authors",
        blank=True,
    )
    slug = models.CharField(
        max_length=61,
        null=False,
        blank=False,
        default=uuid.uuid4,  # vygeneruje nejaky unique kluc
    )

    def __str__(self):
        return f'{self.name} {self.surname}'

# spravit model pre spravu "notifikacia" pre usera a cez foreign key naviazat na usera