from django.db import models
from datetime import date

# Create your models here.
class Port(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    DEGREE_CHOICES=(
        ('BTECH','BTECH'),
        ('BS','BS'),
        ('MTECH','MTECH'),
    )
    POPULAR_SKILL_CHOICES=(
        ('C','C'),
        ('C++','C++'),
        ('JAVA','JAVA'),
        ('PYTHON','PYTHON'),
        ('.NET','.NET'),
        ('javascript','javascript'),
    )
    image = models.ImageField(upload_to='pics/',blank=True,null=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sex=models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    date_of_birth = models.DateField(default=date.today)
    tpercentage = models.DecimalField(decimal_places=2,max_digits=4)
    graduated = models.BooleanField(default=True)
    degree=models.CharField(choices=DEGREE_CHOICES,max_length=5,default='BTECH')
    degree_percentage=models.DecimalField(default=44,decimal_places=2,max_digits=5)
    skills = models.TextField(blank=True,null=True,max_length=100)
    specified_skills = models.CharField(default='C',max_length=20,choices = POPULAR_SKILL_CHOICES)
    add_cv = models.FileField(null = True,blank = True)
    upload_video = models.FileField(upload_to='pics/',blank=True,null=True)

    def __str__(self):
        return self.firstname
