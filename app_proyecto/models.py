from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

def __str__(self):
  return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Mascota(models.Model):
  nombre = models.CharField(max_length=100)
  dueño = models.CharField(max_length=200)
  raza = models.CharField(max_length=100)

def __str__(self):
  return f"{self.nombre}, {self.raza}, {self.id}"

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    dueño = models.CharField(max_length=200)
    numero_patente = models.IntegerField()

def __str__(self):
  return f"{self.marca}, {self.numero_patente}, {self.id}"
