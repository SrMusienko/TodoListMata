from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    done = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        deadline_str = self.deadline.strftime(
            "%Y-%m-%d %H:%M:%S"
        ) if self.deadline else "No deadline"
        return f"{self.content[:10]} - deadline at: {deadline_str}"
