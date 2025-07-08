from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False)
    emailid = models.EmailField(unique=True, blank=False, null=False)
    mobileNumber = models.DecimalField(decimal_places=0, max_digits=10, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    DOB = models.DateField()
    CC = (
        ('IND', 'INDIA'),
          ('US', 'UNITED STATES'),
          ('UK', 'UNITED KINGDOM'),
          ('MEX', 'MEXICO'),
          ('CHN', 'CHINA'),
          ('PAK', 'PAKISTAN'),
          ('AFG', 'AFGANISTAN'),
          ('ALG', 'ALGERIA'),
          ('INA', 'INDONESIA'),
          ('IRN', 'IRAN'),
          ('QTR', 'QATAR'),
          ('RUS', 'RUSSIA'),
          ('SPN', 'SPAIN'),
          ('TURK', 'TURKEY'),
          ('AUS', 'AUSTRALIA'),
          ('BRZ', 'BRAZIL'),
          ('FRANCE', 'FRANCE'),
          ('GER', 'GERMANY'),
          ('JPN', 'JAPAN'),
          ('PL','PALESTINE'),
          ('YEMEN','YEMEN')
    )
    country = models.CharField(max_length=30, choices=CC)
    bio = models.TextField(blank=True, null=True)
