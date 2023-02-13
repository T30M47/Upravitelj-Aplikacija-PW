import factory
from factory.django import DjangoModelFactory
import factory.fuzzy
from main.models import *

class StudentFactory(DjangoModelFactory):
    class Meta:
        model=Student
    
    student_ime=factory.Faker("first_name")
    student_prezime=factory.Faker("last_name")
    student_email=factory.Faker("free_email")

class AplikacijaFactory(DjangoModelFactory):
    class Meta:
        model=Aplikacija
    
    aplikacija_naziv=factory.Faker("sentence", nb_words=4)
    aplikacija_opis=factory.Faker("sentence", nb_words=30)
    aplikacija_datum=factory.Faker("date_time")
    aplikacija_URL=factory.Faker("url")
    aplikacija_AkGod=factory.fuzzy.FuzzyInteger(2000, 2100)
    aplikacija_slika=factory.Faker("image_url")
    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for student in extracted:
                self.students.add(student)
