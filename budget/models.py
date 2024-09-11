from django.db import models

# Create your models here.
class BudgetReal(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  

class SubCategory(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  

class Period(models.Model):
  name = models.CharField(max_length=50)
  multiplier =models.FloatField(default=1)

  def __str__(self):
    return f"{self.name} -  X{self.multiplier}"
  

class Flux(models.Model):
  budget_or_real = models.ForeignKey(BudgetReal, models.SET_NULL, null=True)
  year = models.IntegerField(default=2024)
  date = models.DateField(blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
  period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True)
  amount = models.FloatField(default=0)
  annual_amount = models.FloatField(default=0)
  
  def __str__(self):
    return f"{self.budget_or_real} ({self.year}) -  {self.category}/{self.subcategory}"