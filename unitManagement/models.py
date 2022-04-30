from django.db import models

class Leasing_Info(models.Model):
    leasing_type = models.CharField(max_length=50)
    is_sub_leasing_allowed = models.BooleanField()
    application_fee = models.DecimalField(max_digits=20, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=20, decimal_places=2)
    monthly_rent_1month_lease = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    monthly_rent_6month_lease = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    monthly_rent_12month_lease =models.DecimalField(max_digits=20, decimal_places=2, null=True)
    is_lease_termination_allowed = models.BooleanField()
    lease_termination_cost = models.DecimalField(max_digits=20, decimal_places=2)
    additional_leasing_clauses = models.TextField(null=True)

class Address(models.Model):
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=48)
    county = models.CharField(max_length=25)
    zip = models.CharField(max_length=15)

class UnitType(models.Model):
    unit_type = models.CharField(max_length=50)

class Community(models.Model):
    address_id = models.ForeignKey(Address, null=True, on_delete= models.SET_NULL)
    community_name = models.CharField(max_length=50)

class Unit(models.Model):
    unit_type_id = models.ForeignKey(UnitType, null=True, on_delete= models.SET_NULL)
    community_id = models.ForeignKey(Community, null=True, on_delete= models.SET_NULL)
    address_id = models.ForeignKey(Address, null=True, on_delete= models.SET_NULL)
    leasing_info_id = models.ForeignKey(Leasing_Info, null=True, on_delete= models.SET_NULL) 

    num_of_bedrooms = models.IntegerField()
    num_of_bathrooms =  models.IntegerField()
    num_of_balcony =  models.IntegerField()
    is_available = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)
    unit_availability_start_date = models.DateField(null=True)
    unit_availability_end_date = models.DateField(null=True)
    unit_description = models.TextField(blank=True, null=True)
    living_area_sf = models.IntegerField()
    unit_number = models.IntegerField(null=True)
    unit_at_floor =  models.IntegerField(null=True)




