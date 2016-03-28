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


class TCustomerMstr(models.Model):
    customer_id = models.CharField(db_column='Customer_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=3, blank=True)  # Field name made lowercase.
    customer_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(db_column='City', max_length=35, blank=True)  # Field name made lowercase.
    region = models.CharField(max_length=3, blank=True)
    central_order_block = models.CharField(max_length=2, blank=True)
    central_delivery_block = models.CharField(db_column='Central_delivery_block', max_length=2, blank=True)  # Field name made lowercase.
    central_deletion_flag = models.CharField(db_column='Central_deletion_flag', max_length=1, blank=True)  # Field name made lowercase.
    central_posting_block = models.CharField(db_column='Central_posting_block', max_length=1, blank=True)  # Field name made lowercase.
    central_sales_block = models.CharField(db_column='Central_sales_block', max_length=2, blank=True)  # Field name made lowercase.
    default_sold_id = models.CharField(db_column='DEFAULT_SOLD_ID', max_length=1, blank=True)  # Field name made lowercase.
    legal_status = models.CharField(db_column='Legal_status', max_length=2, blank=True)  # Field name made lowercase.
    times_tamp = models.DateTimeField(db_column='TIMES_TAMP', blank=True, null=True)  # Field name made lowercase.
    pdp_days = models.CharField(db_column='PDP_DAYS', max_length=30, blank=True)  # Field name made lowercase.
    tier = models.CharField(db_column='TIER', max_length=15, blank=True)  # Field name made lowercase.
    credit_limit = models.FloatField(db_column='CREDIT_LIMIT', blank=True, null=True)  # Field name made lowercase.
    customer_gus = models.ForeignKey('GlobalUsers', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CUSTOMER_MSTR'


class ProductList(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, blank=True)
    product_price = models.CharField(max_length=100, blank=True)
    product_isused = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_list'



