from datetime import date

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateField(default=date.today)
    deadline = models.DateField(default=date.today, null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.content} (till {self.deadline})"
