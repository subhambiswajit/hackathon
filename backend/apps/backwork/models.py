from django.db import models

# Create your models here.
class GlobalUsers(models.Model):
    gus_userid = models.IntegerField(primary_key=True)
    gus_username =models.CharField(max_length=30)
    gus_password = models.CharField(max_length=100)
    last_login = models.DateTimeField(db_column='gus_last_login',blank=True, null=True, auto_now_add = True)
    gus_email = models.CharField(max_length=100, blank=True)
    gus_address = models.CharField(max_length=100, blank=True)
    gus_phone = models.CharField(max_length=30, blank=True)
    gus_createdon = models.DateTimeField(blank=True, null=True)
    gus_isused = models.IntegerField(blank=True, null=True)
    gus_confirmcode = models.CharField(max_length=30, blank=True)
    gus_pincode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_users'

