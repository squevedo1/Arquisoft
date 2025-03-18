from django.db import models

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    TIPO_SANGRE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    tipo_de_sangre = models.CharField(max_length=3, choices=TIPO_SANGRE_CHOICES) 
    alergias = models.TextField(blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
