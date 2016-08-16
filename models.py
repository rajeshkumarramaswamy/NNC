from django.db import models


class Noc(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Partner(models.Model):
    name = models.CharField(max_length=50)
    noc = models.ForeignKey(Noc)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    partner = models.ForeignKey(Partner)
    noc = models.ForeignKey(Noc)

    def __str__(self):
        return self.name


