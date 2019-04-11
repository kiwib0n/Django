from django.db import models

class Faculty(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    simple_name = models.CharField(max_length=100)

class Cafedra(models.Model):
    def __str__(self):
        return self.name

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    simple_name = models.CharField(max_length=100)

class Group(models.Model):
    def __str__(self):
        return self.name

    cafedra = models.ForeignKey(Cafedra, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
