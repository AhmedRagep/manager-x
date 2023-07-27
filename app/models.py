from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

# serial=(
#     ("1000", "1000"),
#     ("1001", "1001"),
#     ("1002", "1002"),
#     ("1003", "1003"),
#     ("1004", "1004"),
#     ("1005", "1005"),
#     ("1006", "1006"),
#     ("1007", "1007"),
#     ("1008", "1008"),
# )

MONTH = (
    ('يناير 1', 'January'),
    ('فبراير 2','February'),
    ('مارس 3' ,'March') ,

)

class Person(models.Model):
    code      = models.IntegerField(null=True)
    name      = models.CharField(max_length=100)
    month     = models.CharField(max_length=50,default='')
    year      = models.CharField(max_length=50,default='')
    created_at=models.DateTimeField(default=timezone.now)
    Basic     = models.CharField(max_length=100,default='')
    nature    = models.CharField(max_length=100,default='')
    communications= models.CharField(max_length=100,default='')
    meal      = models.CharField(max_length=100,default='')
    phone     = models.CharField(max_length=100,default='')
    Total     = models.CharField(max_length=100,default='')
    Bonuses   = models.CharField(max_length=100,default='')
    extra     = models.CharField(max_length=100,default='')
    Other_allowances = models.CharField(max_length=100,default='')
    Total_accruals   = models.CharField(max_length=100,default='')
    Sanctions = models.CharField(max_length=100,default='')
    Absences  = models.CharField(max_length=100,default='')
    Insurances = models.CharField(max_length=100,default='')
    income_tax = models.CharField(max_length=100,default='')
    Medical_service= models.CharField(max_length=100,default='')
    Loans = models.CharField(max_length=100,default='')
    Discounts= models.CharField(max_length=100,default='')
    car= models.CharField(max_length=100,default='')
    another= models.CharField(max_length=100,default='')
    Total_deductions= models.CharField(max_length=100,default='')
    Net_salary_payable= models.CharField(max_length=100,default='')
    personal_loan= models.CharField(max_length=100,default='')
    net= models.CharField(max_length=100,default='')
    Reward_days= models.CharField(max_length=100,default='')
    Overtime_hours= models.CharField(max_length=100,default='')
    Absence_with_permission= models.CharField(max_length=100,default='')
    Late_hours= models.CharField(max_length=100,default='')

    def __str__(self):
        return str(self.name) + " " + str(self.code)

# class Serial(models.Model):
#     serialnumer = models.()