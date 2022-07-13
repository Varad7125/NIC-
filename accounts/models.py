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


