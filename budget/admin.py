from django.contrib import admin
from budget.models import BudgetReal, Category, SubCategory, Period, Flux

# Register your models here.
admin.site.register(BudgetReal)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Period)
admin.site.register(Flux)