from django.db import models

# Create your models here.

class Student(models.Model):
    student_ime=models.CharField(max_length=50)
    student_prezime=models.CharField(max_length=50)
    student_email=models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.student_ime, self.student_prezime)

class Aplikacija(models.Model):
    aplikacija_naziv=models.CharField(max_length=100)
    aplikacija_opis=models.TextField()
    aplikacija_datum=models.DateField()
    aplikacija_URL=models.URLField(null=True,blank=True,)
    aplikacija_AkGod=models.CharField(max_length=30)
    aplikacija_slika=models.ImageField(null=True, blank=True, upload_to='media')
    aplikacija_slika1=models.ImageField(null=True, blank=True, upload_to='media')
    aplikacija_slika2=models.ImageField(null=True, blank=True, upload_to='media')
    aplikacija_slika3=models.ImageField(null=True, blank=True, upload_to='media')
    aplikacija_slika4=models.ImageField(null=True, blank=True, upload_to='media')
    aplikacija_student=models.ManyToManyField(Student)

    def __str__(self):
        return self.aplikacija_naziv