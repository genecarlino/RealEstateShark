from django.db import models
from django.forms import DateField
from leaseManagement.models import Unit_Lease, Application

class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_role = models.CharField(max_length=50)
    employment_start_date = DateField()
    employment_end_date = DateField()
    staff_notes = models.TextField(null=True,blank=True)

class Service_Category(models.Model):
    service_category = models.TextField(null=True,blank=True)

class Service_Request(models.Model):
    unit_lease = models.ForeignKey(Unit_Lease, null=True, on_delete= models.SET_NULL)
    Service_Category = models.ForeignKey(Service_Category, null=True, on_delete= models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete= models.SET_NULL)

    problem_description = models.TextField()
    log_date = models.DateTimeField(auto_now_add=True)
    closure_date = models.DateField()

class rent_payment_log(models.Model):
    unit_lease = models.ForeignKey(Unit_Lease, null=True, on_delete= models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete= models.SET_NULL)

    amount_paid = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    payment_medium = models.TextField()
    payment_date = models.DateTimeField(auto_now_add=True)
    check_number = models.IntegerField(null=True)
    online_transaction_number = models.IntegerField(null=True)

class Staff_APP_Join(models.Model):
    staff = models.ForeignKey(Staff, null=True, on_delete= models.SET_NULL)
    application = models.ForeignKey(Application, null=True, on_delete= models.SET_NULL)




    


