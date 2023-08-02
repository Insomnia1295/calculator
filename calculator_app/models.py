from django.db import models

from django.db import models

class Calculator(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    
    def add(self):
        return self.number1 + self.number2
    
    def subtract(self):
        return self.number1 - self.number2
    
    def multiply(self):
        return self.number1 * self.number2
    
    def divide(self):
        if self.number2 != 0:
            return self.number1 / self.number2
        else:
            raise ZeroDivisionError("Cannot divide by zero.")
# Create your models here.
