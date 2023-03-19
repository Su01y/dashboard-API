from django.db import models


class Aspirant(models.Model):

    RANG = (
        ('0', 'no rang'),
        ('1', 'junior'),
        ('2', 'middle'),
        ('3', 'senior'),
        ('4', 'team lead'),
    )

    EDUCATION = (
        ('0', 'high scool'),
        ('1', 'college'),
        ('2', 'bachelor'),
        ('3', 'specialist'),
        ('4', 'master'),
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.TextField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER)
    exp = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    technologies = models.ManyToManyField('Technologies', blank=True, null=True, related_name='aspirants')
    gpa = models.FloatField()
    education = models.CharField(max_length=2, choices=EDUCATION, default='high scool')
    achievenments = models.TextField(max_length=5000, blank=True, null=True)
    hobbies = models.TextField(max_length=5000, blank=True, null=True)
    rang = models.CharField(max_length=2, choices=RANG, default='no rang')
    score = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.score = int(self.rang) * 74 + int(self.education) * 33 + self.exp * 89 + int(pow(self.gpa, 3))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-score']


class Technologies(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name
