from django.db import models


priorty_choises = [
    (1, 'high'),
    (2, 'medium'),
    (3, 'low'),
]
status_choises = [
    ('c', 'completed'),
    ('w', 'waiting'),
    ('p', 'no progress')
]


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    priority = models.SmallIntegerField(choices=priorty_choises, default=3)
    status = models.CharField(
        max_length=1, choices=status_choises, default='p')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
