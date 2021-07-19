from django.db import models
'''
class newTableName(models.Model): #table name must be singuler
    clmn_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.clmn_name
'''

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name