import email
from django.db import models
from django.contrib.auth.models import User
from numpy import character


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class nic_admin(models.Model):
    name = models.TextField()
    uid = models.TextField(primary_key=True)
    mobile = models.CharField(max_length=10)
    email = models.TextField()

class state_admin(models.Model):
    joint_commissioner = models.TextField()
    creation_timestamp = models.DateTimeField()
    uid = models.CharField(max_length=6 , primary_key=True)
    mobile = models.CharField(max_length=10)
    email = models.TextField()


class districts(models.Model):
    sr_no = models.IntegerField()
    district_code = models.CharField(max_length=3, primary_key=True)
    district_name_eng = models.TextField()
    district_name_local = models.TextField()
    census_2001 = models.CharField(max_length=2)
    census_2011 = models.CharField(max_length=3)
    district_version = models.CharField(max_length=1)


class district_collectors(models.Model):
    sr_no = models.IntegerField()
    collector_name = models.CharField(max_length=100)
    collector_code = models.CharField(max_length=10 , primary_key=True)
    district = models.CharField(max_length=100)
    creation_timestamp = models.DateTimeField()
    is_active = models.CharField(max_length=1)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=20)


class tehsil(models.Model):
    sr_no = models.IntegerField()
    tehsil_code = models.CharField(max_length=3, primary_key=True)
    tehsil_name_eng = models.TextField()
    tehsil_name_local = models.TextField()
    census_2001 = models.CharField(max_length=2)
    census_2011 = models.CharField(max_length=3)
    tehsil_version = models.CharField(max_length=1)
    district_code = models.CharField(max_length=3)


class tehsildars(models.Model):
    sr_no = models.IntegerField()
    tehsildar_name = models.CharField(max_length=100)
    tehsildar_code = models.CharField(max_length=10 , primary_key=True)
    district = models.CharField(max_length=100)
    creation_timestamp = models.DateTimeField()
    is_active = models.CharField(max_length=1)
    tehsil_code = models.TextField()
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=20)



class farmer_new(models.Model):
    sr_no = models.IntegerField(default=True)
    pm_kisan_id = models.CharField(max_length=11, default=True)
    aadhaar_no = models.CharField(max_length=12,default=True, primary_key=True)
    bank_ifsc = models.CharField(max_length=11, default=True)
    bank_acc_number = models.CharField(max_length=16, default=True)
    username = models.TextField(default=True)
    createdby_tehsildar = models.TextField(default=True)
    farmer_name = models.CharField(max_length=100,default=True)
    farmer_father_name = models.TextField(default=True)
    khata_number = models.IntegerField(default=True)
    khasra_number = models.TextField(default=True)
    is_active = models.CharField(max_length=1, default=True)
    state_code = models.CharField(max_length=20, default=True)
    district_code = models.CharField(max_length=100, default=True)
    tehsil_code = models.CharField(max_length=4, default=True)
    land_area_unit = models.TextField(max_length=100, default=True)
    land_area = models.TextField(max_length=50, default=True)
    creation_timestamp = models.DateTimeField(default=True)
    land_block_code = models.TextField(default=True)
    land_location = models.CharField(max_length=100, default=True)
    type_of_mutation = models.CharField(max_length=100, default=True)
    date_of_mutation= models.DateField(default=True)
    land_ownership_type = models.TextField(default=True)