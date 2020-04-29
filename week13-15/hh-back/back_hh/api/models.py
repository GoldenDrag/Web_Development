from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default='')
    city = models.CharField(max_length=40)
    address = models.TextField(default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return str(self.id)


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default='')
    salary = models.FloatField(default=0.0)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company_id': self.company_id.id
        }

    def __str__(self):
        return self.name
