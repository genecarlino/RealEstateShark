from django.db import models
from unitManagement.models import Unit

class Renter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identity_proof_document = models.CharField(max_length=100)
    identity_proof = models.CharField(max_length=100)
    permenant_address = models.TextField()

class Application(models.Model):
    renter =  models.ForeignKey(Renter, null=True, on_delete= models.SET_NULL)
    unit =  models.ForeignKey(Unit, null=True, on_delete= models.SET_NULL)
    requirement = models.CharField(max_length = 100, null= True)
    submit_date = models.DateTimeField(auto_now_add=True)
    processing_date = models.DateTimeField(null=True)
    processing_status = models.CharField(max_length=75, null=True, blank=True)

class Unit_Lease(models.Model):
    application =  models.ForeignKey(Application, null=True, on_delete= models.SET_NULL)
    unit =  models.ForeignKey(Unit, null=True, on_delete= models.SET_NULL)

    lease_tenure_in_months = models.IntegerField(default=10)
    monthly_rent = models.DecimalField(max_digits=20, decimal_places=2)
    discount_in_rent = models.DecimalField(max_digits=20, decimal_places=2)
    lease_starting_from = models.DateField(null = True)
    lease_ending_on = models.DateField(null = True)






