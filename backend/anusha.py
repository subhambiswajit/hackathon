# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class TCalendarInfo(models.Model):
    customer = models.ForeignKey('TCustomerMstr', db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    rs_name = models.CharField(db_column='RS_Name', max_length=100, blank=True)  # Field name made lowercase.
    channel = models.CharField(db_column='Channel', max_length=4, blank=True)  # Field name made lowercase.
    business = models.CharField(db_column='Business', max_length=10, blank=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=10, blank=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=125, blank=True)  # Field name made lowercase.
    moc = models.IntegerField(db_column='MOC', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.CharField(db_column='Activity_Type', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CALENDAR_INFO'


class TCapitalProjection(models.Model):
    customer = models.ForeignKey('TCustomerMstr', db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    rs_name = models.CharField(db_column='RS_Name', max_length=100, blank=True)  # Field name made lowercase.
    channel = models.CharField(db_column='Channel', max_length=10, blank=True)  # Field name made lowercase.
    business = models.CharField(db_column='Business', max_length=10, blank=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=10, blank=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=25, blank=True)  # Field name made lowercase.
    moc = models.IntegerField(db_column='MOC', blank=True, null=True)  # Field name made lowercase.
    rs_sales = models.IntegerField(db_column='RS_Sales', blank=True, null=True)  # Field name made lowercase.
    rs_sales_forecast = models.IntegerField(db_column='RS_Sales_forecast', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CAPITAL_PROJECTION'


class TChequeUtilization(models.Model):
    customer = models.ForeignKey('TCustomerMstr', db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    accounting_clerk = models.CharField(db_column='ACCOUNTING_CLERK', max_length=20, blank=True)  # Field name made lowercase.
    cheque_book_no_from = models.IntegerField(db_column='CHEQUE_BOOK_NO_FROM', blank=True, null=True)  # Field name made lowercase.
    cheque_book_no_to = models.IntegerField(db_column='CHEQUE_BOOK_NO_TO', blank=True, null=True)  # Field name made lowercase.
    cheque_num_utilized = models.IntegerField(db_column='CHEQUE_NUM_UTILIZED', blank=True, null=True)  # Field name made lowercase.
    billing_document_number = models.CharField(db_column='BILLING_DOCUMENT_NUMBER', max_length=20, blank=True)  # Field name made lowercase.
    billing_date = models.DateField(db_column='BILLING_DATE', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    cheque_date = models.DateField(db_column='CHEQUE_DATE', blank=True, null=True)  # Field name made lowercase.
    clearing_doc = models.CharField(db_column='CLEARING_DOC', max_length=10, blank=True)  # Field name made lowercase.
    document_no = models.CharField(db_column='DOCUMENT_NO', max_length=10, blank=True)  # Field name made lowercase.
    doc_type = models.CharField(db_column='DOC_TYPE', max_length=2, blank=True)  # Field name made lowercase.
    receipt_document_no = models.CharField(db_column='RECEIPT_DOCUMENT_NO', max_length=20, blank=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    banking_date = models.DateField(db_column='BANKING_DATE', blank=True, null=True)  # Field name made lowercase.
    house_bank = models.CharField(db_column='HOUSE_BANK', max_length=5, blank=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='ACCOUNT_ID', max_length=5, blank=True)  # Field name made lowercase.
    pay_in_slip_number = models.IntegerField(db_column='PAY_IN_SLIP_NUMBER', blank=True, null=True)  # Field name made lowercase.
    pay_in_slip_date = models.DateField(db_column='PAY_IN_SLIP_DATE', blank=True, null=True)  # Field name made lowercase.
    pay_in_slip_type = models.CharField(db_column='PAY_IN_SLIP_TYPE', max_length=6, blank=True)  # Field name made lowercase.
    cheque_deposit_date = models.DateField(db_column='CHEQUE_DEPOSIT_DATE', blank=True, null=True)  # Field name made lowercase.
    creation_date = models.DateField(db_column='CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CHEQUE_UTILIZATION'


class TCustomerMstr(models.Model):
    customer_id = models.CharField(db_column='Customer_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=3, blank=True)  # Field name made lowercase.
    customer_name = models.CharField(max_length=35, blank=True)
    city = models.CharField(db_column='City', max_length=35, blank=True)  # Field name made lowercase.
    region = models.CharField(max_length=3, blank=True)
    central_order_block = models.CharField(max_length=2, blank=True)
    central_delivery_block = models.CharField(db_column='Central_delivery_block', max_length=2, blank=True)  # Field name made lowercase.
    central_deletion_flag = models.CharField(db_column='Central_deletion_flag', max_length=1, blank=True)  # Field name made lowercase.
    central_posting_block = models.CharField(db_column='Central_posting_block', max_length=1, blank=True)  # Field name made lowercase.
    central_sales_block = models.CharField(db_column='Central_sales_block', max_length=2, blank=True)  # Field name made lowercase.
    default_sold_id = models.CharField(db_column='DEFAULT_SOLD_ID', max_length=1, blank=True)  # Field name made lowercase.
    legal_status = models.CharField(db_column='Legal_status', max_length=2, blank=True)  # Field name made lowercase.
    times_tamp = models.DateTimeField(db_column='TIMES_TAMP')  # Field name made lowercase.
    pdp_days = models.CharField(db_column='PDP_DAYS', max_length=30, blank=True)  # Field name made lowercase.
    tier = models.CharField(db_column='TIER', max_length=15, blank=True)  # Field name made lowercase.
    credit_limit = models.FloatField(db_column='CREDIT_LIMIT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CUSTOMER_MSTR'


class TDeliveryInfo(models.Model):
    delivery_date = models.DateField(db_column='DELIVERY_DATE', blank=True, null=True)  # Field name made lowercase.
    delivery_id = models.CharField(db_column='DELIVERY_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    delivery_type = models.CharField(db_column='DELIVERY_TYPE', max_length=4, blank=True)  # Field name made lowercase.
    shipping_point = models.CharField(db_column='SHIPPING_POINT', max_length=4, blank=True)  # Field name made lowercase.
    ship_to_party = models.CharField(db_column='SHIP_TO_PARTY', max_length=10, blank=True)  # Field name made lowercase.
    total_weight = models.FloatField(db_column='TOTAL_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    release_type = models.CharField(db_column='RELEASE_TYPE', max_length=4, blank=True)  # Field name made lowercase.
    planning_flag = models.CharField(db_column='PLANNING_FLAG', max_length=2, blank=True)  # Field name made lowercase.
    created_on = models.DateField(db_column='CREATED_ON', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=12, blank=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME')  # Field name made lowercase.
    sales_org = models.CharField(db_column='SALES_ORG', max_length=4, blank=True)  # Field name made lowercase.
    order_combination = models.CharField(db_column='ORDER_COMBINATION', max_length=1, blank=True)  # Field name made lowercase.
    pick_date = models.DateField(db_column='PICK_DATE', blank=True, null=True)  # Field name made lowercase.
    unloading_point = models.CharField(db_column='UNLOADING_POINT', max_length=25, blank=True)  # Field name made lowercase.
    incot = models.CharField(db_column='INCOT', max_length=3, blank=True)  # Field name made lowercase.
    route = models.CharField(db_column='ROUTE', max_length=6, blank=True)  # Field name made lowercase.
    sold_to_party = models.CharField(db_column='SOLD_TO_PARTY', max_length=10, blank=True)  # Field name made lowercase.
    net_weight = models.FloatField(db_column='NET_WEIGHT', blank=True, null=True)  # Field name made lowercase.
    confirmation_status = models.CharField(db_column='CONFIRMATION_STATUS', max_length=1, blank=True)  # Field name made lowercase.
    delivery_status = models.CharField(db_column='DELIVERY_STATUS', max_length=1, blank=True)  # Field name made lowercase.
    transportation_status = models.CharField(db_column='TRANSPORTATION_STATUS', max_length=1, blank=True)  # Field name made lowercase.
    confirmed_date = models.DateField(db_column='CONFIRMED_DATE', blank=True, null=True)  # Field name made lowercase.
    transport_date = models.DateField(db_column='TRANSPORT_DATE', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(TCustomerMstr, db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    invoice_amount = models.IntegerField(db_column='INVOICE_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='PRODUCT', max_length=200, blank=True)  # Field name made lowercase.
    product_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_DELIVERY_INFO'


class TIncidentInfo(models.Model):
    incident_id = models.IntegerField(db_column='Incident_ID', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=25, blank=True)  # Field name made lowercase.
    incident_type = models.CharField(db_column='Incident_type', max_length=15, blank=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=50, blank=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=15, blank=True)  # Field name made lowercase.
    created_on = models.DateField(db_column='Created_On', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=25, blank=True)  # Field name made lowercase.
    solution_details = models.CharField(db_column='Solution_Details', max_length=50, blank=True)  # Field name made lowercase.
    customer = models.ForeignKey(TCustomerMstr, db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_INCIDENT_INFO'


class TInvoiceDetails(models.Model):
    billing_document = models.CharField(db_column='Billing_Document', primary_key=True, max_length=10)  # Field name made lowercase.
    billing_type = models.CharField(db_column='Billing_Type', max_length=4, blank=True)  # Field name made lowercase.
    billing_category = models.CharField(db_column='Billing_category', max_length=1, blank=True)  # Field name made lowercase.
    sales_distribution_doc_type = models.CharField(db_column='SALES_DISTRIBUTION_DOC_TYPE', max_length=1, blank=True)  # Field name made lowercase.
    sales_doc_currency = models.CharField(db_column='SALES_DOC_CURRENCY', max_length=5, blank=True)  # Field name made lowercase.
    sales_organization = models.CharField(db_column='Sales_Organization', max_length=4, blank=True)  # Field name made lowercase.
    distribution_channel = models.CharField(db_column='Distribution_Channel', max_length=2, blank=True)  # Field name made lowercase.
    pricing_procedure = models.CharField(db_column='Pricing_procedure', max_length=6, blank=True)  # Field name made lowercase.
    billing_date = models.DateField(db_column='Billing_Date', blank=True, null=True)  # Field name made lowercase.
    accounting_doc_number = models.CharField(db_column='Accounting_Doc_Number', max_length=10, blank=True)  # Field name made lowercase.
    fiscal_year = models.IntegerField(db_column='Fiscal_Year', blank=True, null=True)  # Field name made lowercase.
    posting_period = models.IntegerField(db_column='Posting_period', blank=True, null=True)  # Field name made lowercase.
    incoterms = models.CharField(db_column='Incoterms', max_length=3, blank=True)  # Field name made lowercase.
    posting_status = models.CharField(db_column='Posting_Status', max_length=1, blank=True)  # Field name made lowercase.
    terms_of_payment = models.CharField(db_column='Terms_of_Payment', max_length=4, blank=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=1, blank=True)  # Field name made lowercase.
    acct_assignment_group = models.CharField(db_column='ACCT_ASSIGNMENT_GROUP', max_length=2, blank=True)  # Field name made lowercase.
    destination_country = models.CharField(db_column='Destination_Country', max_length=3, blank=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=3, blank=True)  # Field name made lowercase.
    county_code = models.CharField(db_column='County_code', max_length=3, blank=True)  # Field name made lowercase.
    city_code = models.CharField(db_column='City_code', max_length=4, blank=True)  # Field name made lowercase.
    company_code = models.ForeignKey('TPaymentInfo', db_column='Company_Code', blank=True, null=True)  # Field name made lowercase.
    net_value = models.FloatField(db_column='Net_Value', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_by', max_length=12, blank=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    created_on = models.FloatField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    payer = models.CharField(db_column='Payer', max_length=10, blank=True)  # Field name made lowercase.
    sold_toparty = models.CharField(db_column='Sold_toparty', max_length=10, blank=True)  # Field name made lowercase.
    vat_registration_no = models.CharField(db_column='VAT_Registration_No', max_length=20, blank=True)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=2, blank=True)  # Field name made lowercase.
    credit_control_area = models.CharField(db_column='Credit_Control_Area', max_length=4, blank=True)  # Field name made lowercase.
    credit_account = models.CharField(db_column='Credit_account', max_length=10, blank=True)  # Field name made lowercase.
    business_place = models.CharField(db_column='Business_Place', max_length=4, blank=True)  # Field name made lowercase.
    sales_order = models.CharField(db_column='Sales_Order', max_length=10, blank=True)  # Field name made lowercase.
    warehouse_number = models.ForeignKey('TWarehouseMstr', db_column='Warehouse_Number', blank=True, null=True)  # Field name made lowercase.
    direct_dispatch = models.CharField(db_column='Direct_Dispatch', max_length=1, blank=True)  # Field name made lowercase.
    customer_id = models.CharField(db_column='Customer_ID', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_INVOICE_DETAILS'


class TPaymentInfo(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=10)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=10, blank=True)  # Field name made lowercase.
    customer = models.ForeignKey(TCustomerMstr, db_column='CUSTOMER_ID')  # Field name made lowercase.
    payment_method_description = models.CharField(db_column='Payment_Method_Description', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PAYMENT_INFO'


class TPendingCreditDebitNote(models.Model):
    company_code = models.CharField(db_column='COMPANY_CODE', max_length=4, blank=True)  # Field name made lowercase.
    customer = models.ForeignKey(TCustomerMstr, db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    transaction_type = models.CharField(db_column='Transaction_Type', max_length=20, blank=True)  # Field name made lowercase.
    document_no = models.CharField(db_column='DOCUMENT_NO', max_length=20, blank=True)  # Field name made lowercase.
    credit_debit_type = models.CharField(db_column='CREDIT_DEBIT_TYPE', max_length=1, blank=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    date_of_document = models.DateField(db_column='DATE_OF_DOCUMENT', blank=True, null=True)  # Field name made lowercase.
    short_desc = models.CharField(db_column='SHORT_DESC', max_length=25, blank=True)  # Field name made lowercase.
    transaction_type_desc = models.CharField(db_column='TRANSACTION_TYPE_DESC', max_length=250, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PENDING_CREDIT_DEBIT_NOTE'


class TPromotionInfo(models.Model):
    promotion_id = models.CharField(db_column='Promotion_ID', max_length=10, blank=True)  # Field name made lowercase.
    promotion_name = models.CharField(db_column='Promotion_Name', max_length=200, blank=True)  # Field name made lowercase.
    promotion_start_date = models.DateField(db_column='Promotion_Start_Date', blank=True, null=True)  # Field name made lowercase.
    promotion_end_date = models.DateField(db_column='Promotion_End_Date', blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=50, blank=True)  # Field name made lowercase.
    business = models.CharField(db_column='Business', max_length=50, blank=True)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=5, blank=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=200, blank=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=10, blank=True)  # Field name made lowercase.
    promotion_status = models.CharField(db_column='Promotion_Status', max_length=20, blank=True)  # Field name made lowercase.
    investment_type = models.CharField(db_column='Investment_Type', max_length=100, blank=True)  # Field name made lowercase.
    moc = models.CharField(db_column='MOC', max_length=20, blank=True)  # Field name made lowercase.
    submission_date = models.DateField(db_column='Submission_Date', blank=True, null=True)  # Field name made lowercase.
    approved_date = models.DateField(db_column='Approved_Date', blank=True, null=True)  # Field name made lowercase.
    planned_investment_amount = models.FloatField(db_column='Planned_Investment_Amount', blank=True, null=True)  # Field name made lowercase.
    customer_0 = models.ForeignKey(TCustomerMstr, db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    region = models.CharField(db_column='REGION', max_length=3, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_PROMOTION_INFO'


class TWarehouseMstr(models.Model):
    warehouse_number = models.CharField(db_column='Warehouse_Number', max_length=3)  # Field name made lowercase.
    plant = models.CharField(db_column='PLANT', max_length=5)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=5)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_WAREHOUSE_MSTR'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GlobalUsers(models.Model):
    gus_userid = models.IntegerField(primary_key=True)
    gus_username = models.IntegerField(blank=True, null=True)
    gus_password = models.CharField(max_length=100)
    gus_last_login = models.DateTimeField(blank=True, null=True)
    gus_email = models.CharField(max_length=100, blank=True)
    gus_address = models.CharField(max_length=100, blank=True)
    gus_phone = models.IntegerField(blank=True, null=True)
    gus_createdon = models.DateTimeField(blank=True, null=True)
    gus_isused = models.IntegerField(blank=True, null=True)
    gus_confirmcode = models.CharField(max_length=30, blank=True)
    gus_pincode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_users'
