from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from datetime import date

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

GENDER_CHOICES =( 
    ("Masculino", "Masculino"), 
    ("Feminino", "Feminino"), 
    ("Prefiro não dizer", "Prefiro não dizer"), 
    ("Outro", "Outro"),
 
)

COR_CHOICES =( 
    ("Amarelo", "Amarelo"), 
    ("Branco", "Branco"), 
    ("Indegena", "Indegena"), 
    ("Pardo", "Pardo"),
    ("Preto", "Preto")
 
)

BIMESTRE_CHOICES=(
    ("1° Bimestre", "1° Bimestre"), 
    ("2° Bimestre", "2° Bimestre"), 
    ("3° Bimestre", "3° Bimestre"), 
    ("4° Bimestre", "4° Bimestre")

)

class School(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=150, null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)
    estado = models.CharField(max_length=20, null=False, blank=False)
    regiao = models.CharField(max_length=150, null=False, blank=False)


class SchoolBoard(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cargo = models.CharField(max_length=100, null=False, blank=False)
    escola = models.ForeignKey(School, on_delete=models.DO_NOTHING)


class Teacher(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    idade = models.DateField()
    genero = models.CharField(max_length=100, choices = GENDER_CHOICES)
    corouraca = models.CharField(max_length=100, choices = COR_CHOICES)
    escola = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    disciplina = models.ManyToManyField('SchoolSubject', related_name='teacher')

    def calculate_age(self):
        today = date.today()
        age = today.year - self.idade.year - ((today.month, today.day) < (self.idade.month, self.idade.day))
        return age
    

class Student(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    idade = models.DateField()
    genero = models.CharField(max_length=100, choices = GENDER_CHOICES)
    corouraca = models.CharField(max_length=100, choices = COR_CHOICES)
    escola = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    turma = models.ForeignKey('Class', on_delete=models.DO_NOTHING)

    def calculate_age(self):
        today = date.today()
        age = today.year - self.idade.year - ((today.month, today.day) < (self.idade.month, self.idade.day))
        return age
    

class SchoolSubject(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    professor = models.ManyToManyField(Teacher, related_name='subjects')
    student = models.ManyToManyField(Student, related_name='subjects')

class Class(models.Model):
    serie = models.CharField(max_length=20)
    professor = models.ManyToManyField('Teacher', related_name='turma')


class Lesson(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=False)
    licao = models.FileField(upload_to="licoes/")
    turma = models.ForeignKey('Class', on_delete=models.DO_NOTHING)

#Frequencia  
class Attendance(models.Model):
    aluno = models.ForeignKey('Student', on_delete=models.DO_NOTHING)
    periodo = models.CharField(max_length=200, choices = BIMESTRE_CHOICES)
    ano_letivo = models.DateField()
    

    

