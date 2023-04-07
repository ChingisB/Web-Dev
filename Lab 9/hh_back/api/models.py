from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    city = models.CharField(max_length=20)
    address = models.TextField()

    def to_json(self):
        new_object = {}
        new_object['name'] = self.name
        new_object['decription'] = self.description
        new_object['city'] = self.city
        new_object['address'] = self.address
        return new_object

    @staticmethod
    def list_to_json(objects):
        return list(map(Company.to_json, objects))


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def to_json(self):
        new_object = {}
        new_object['name'] = self.name
        new_object['decription'] = self.description
        new_object['salary'] = self.salary
        new_object['company'] = self.company.to_json()
        return new_object

    @staticmethod
    def list_to_json(objects):
        return list(map(Vacancy.to_json, objects))
