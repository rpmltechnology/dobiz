
from django.db import models
from decimal import Decimal
# Create your models here.
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from django.utils import timezone
# from django.utils.translation import activate, ugettext_lazy as _
from . manager import UserManager
from django.contrib.auth.models import PermissionsMixin
from django_countries.fields import CountryField
from django.contrib.auth.models import Group
import datetime

class Page(models.Model):
    pagename = models.CharField(max_length=200,null=True, blank=True)
    pagetitle = models.CharField(max_length=200,null=True, blank=True)
    section = models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self):
        return self.pagetitle

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=14)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    otp = models.CharField(max_length=6,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    otp_for_mobile = models.CharField(max_length=6,blank=True,null=True)
    otp_for_forgot_pass = models.CharField(max_length=6,blank=True,null=True)
    refer_by = models.CharField(max_length=111, default="admin@dobiz.com")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=20,null=True, blank=False)
    email = models.CharField(max_length=255,null=True, blank=False)
    phone = models.CharField(max_length=14,null=True, blank=False)
    state = models.CharField(max_length=14,null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING,null=True,blank=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    mobile = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=255, unique=True)
    Services = models.BooleanField(default=False)
    Business = models.BooleanField(default=False)
    Think_to_start_business = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = CountryField(blank=True)
    pin = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    def __str__(self):
        return self.fname + self.email

class Product(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    product_name = models.CharField(max_length=50,null=True, blank=False)
    category = models.CharField(max_length=50, default="", null=True, blank=True)
    subcategory = models.CharField(max_length=50, default="", null=True, blank=True)
    market_price = models.CharField(max_length =10, null=True, blank=False)
    discounted_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Dobiz_India_Filings = models.IntegerField( null=True,blank=True)
    gst_percent = models.IntegerField(null=True, blank=True,default=18)
    gst  =models.IntegerField(null=True, blank=True)
    other_cost = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    estimated_delivery_days = models.PositiveIntegerField(null=True, blank=True)
    pub_date = models.DateField(null=True, blank=False)
    img1 = models.ImageField(null=True, blank=True, default='/common_img.png')
    is_package = models.BooleanField(null=True, blank=True) 
    @property
    def estimated_delivery_date(self):
        if self.estimated_delivery_days:
            return datetime.date.today() + datetime.timedelta(days=self.estimated_delivery_days)
        else:
            return None

    @estimated_delivery_date.setter
    def estimated_delivery_date(self, value):
        pass
    def save(self, *args, **kwargs):
        if self.discounted_percentage:
            self.Dobiz_India_Filings = Decimal(self.market_price) * (Decimal('1') - Decimal(self.discounted_percentage) / Decimal('100'))
            self.gst = self.Dobiz_India_Filings * Decimal(self.gst_percent) / Decimal('100')
            self.price = self.gst + self.Dobiz_India_Filings
            if self.other_cost:
                self.price += self.other_cost
        else:
            self.price = Decimal(self.market_price)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
        
    

class Coupan(models.Model):
    coupan = models.CharField(max_length=20,unique=True)
    amount = models.IntegerField(null=True,blank=True)
    active = models.IntegerField(default=0)
    percentage = models.IntegerField(null=True,blank=True)
    username = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True,blank=True)
    commissionpaid = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.coupan

class Order(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False)
    is_cart = models.IntegerField(default=1, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True,blank= True)
    email = models.EmailField(null=True, blank=True)
    address1 = models.CharField(max_length=200, null=True,blank= True)
    address2 = models.CharField(max_length=200, null=True,blank= True)
    address3 = models.CharField(max_length=200, null=True,blank= True)
    remarks = models.CharField(max_length=300, null=True, blank=True)
    buy_time = models.DateTimeField(null=True, blank=True)
    order_time = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(null=True, blank=True)
    coupan = models.ForeignKey(to=Coupan, null=True, blank=True,on_delete=models.SET_NULL)
    sell_price = models.IntegerField(null=True,blank=True)
    razor_pay_order_id = models.CharField(max_length=100,null=True,blank=True)
    razor_payment_id = models.CharField(max_length=100,null=True,blank=True)
    razor_payment_signature = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.product.product_name} {self.user.name}"
    def apply_coupon(self, coupon):
        self.coupan = coupon
        print("apply_coupon method called!")
        self.save()
class Banner(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    review_rating = models.CharField(max_length=200,null=True, blank=True)
    review = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)

class Meaning(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    heading_text5 = models.CharField(max_length=200,null=True, blank=True)
    heading_text6 = models.CharField(max_length=200,null=True, blank=True)
    heading_text7 = models.CharField(max_length=200,null=True, blank=True)
    heading_text8 = models.CharField(max_length=200,null=True, blank=True)
    heading_text9 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    text7 = models.TextField(null=True, blank=True)
    text8 = models.TextField(null=True, blank=True)
    text9 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category

class MinimumRequirement(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    list15 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class Benefits(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    text7 = models.TextField(null=True, blank=True)
    text8 = models.TextField(null=True, blank=True)
    text9 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    list15 = models.CharField(max_length=200,blank=True,null=True)
    list16 = models.CharField(max_length=200,blank=True,null=True)
    list17 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class DocumentRequired(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    list15 = models.CharField(max_length=200,blank=True,null=True)
    list16 = models.CharField(max_length=200,blank=True,null=True)
    list17 = models.CharField(max_length=200,blank=True,null=True)
    list18 = models.CharField(max_length=200,blank=True,null=True)
    list19 = models.CharField(max_length=200,blank=True,null=True)
    list20 = models.CharField(max_length=200,blank=True,null=True)
    list21 = models.CharField(max_length=200,blank=True,null=True)
    list22 = models.CharField(max_length=200,blank=True,null=True)
    list23 = models.CharField(max_length=200,blank=True,null=True)
    list24 = models.CharField(max_length=200,blank=True,null=True)
    list25 = models.CharField(max_length=200,blank=True,null=True)
    list26 = models.CharField(max_length=200,blank=True,null=True)
    list27 = models.CharField(max_length=200,blank=True,null=True)
    list28 = models.CharField(max_length=200,blank=True,null=True)
    list29 = models.CharField(max_length=200,blank=True,null=True)
    list30 = models.CharField(max_length=200,blank=True,null=True)
    list31 = models.CharField(max_length=200,blank=True,null=True)
    list32 = models.CharField(max_length=200,blank=True,null=True)
    list33 = models.CharField(max_length=200,blank=True,null=True)
    list34 = models.CharField(max_length=200,blank=True,null=True)
    list35 = models.CharField(max_length=200,blank=True,null=True)
    list36 = models.CharField(max_length=200,blank=True,null=True)
    list37 = models.CharField(max_length=200,blank=True,null=True)
    list38 = models.CharField(max_length=200,blank=True,null=True)
    list39 = models.CharField(max_length=200,blank=True,null=True)
    list40 = models.CharField(max_length=200,blank=True,null=True)
    list41 = models.CharField(max_length=200,blank=True,null=True)
    list42 = models.CharField(max_length=200,blank=True,null=True)
    list43 = models.CharField(max_length=200,blank=True,null=True)
    list44 = models.CharField(max_length=200,blank=True,null=True)
    list45 = models.CharField(max_length=200,blank=True,null=True)
    list46 = models.CharField(max_length=200,blank=True,null=True)
    list47 = models.CharField(max_length=200,blank=True,null=True)
    list48 = models.CharField(max_length=200,blank=True,null=True)
    list49 = models.CharField(max_length=200,blank=True,null=True)
    list50 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class IncorporationProcess(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class Compliance(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    list15 = models.CharField(max_length=200,blank=True,null=True)
    list16 = models.CharField(max_length=200,blank=True,null=True)
    list17 = models.CharField(max_length=200,blank=True,null=True)
    list18 = models.CharField(max_length=200,blank=True,null=True)
    list19 = models.CharField(max_length=200,blank=True,null=True)
    list20 = models.CharField(max_length=200,blank=True,null=True)
    list21 = models.CharField(max_length=200,blank=True,null=True)
    list22 = models.CharField(max_length=200,blank=True,null=True)
    list23 = models.CharField(max_length=200,blank=True,null=True)
    list24 = models.CharField(max_length=200,blank=True,null=True)
    list25 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class Closure(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    heading_text3 = models.CharField(max_length=200,null=True, blank=True)
    heading_text4 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class StepWiseProcedure(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    step1 = models.CharField(max_length=200,null=True, blank=True)
    answer1 = models.TextField(null=True, blank=True)
    step2 = models.CharField(max_length=200,null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    step3 = models.CharField(max_length=200,null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    step4 = models.CharField(max_length=200,null=True, blank=True)
    answer4 = models.TextField(null=True, blank=True)
    step5 = models.CharField(max_length=200,null=True, blank=True)
    answer5 = models.TextField(null=True, blank=True)
    step6 = models.CharField(max_length=200,null=True, blank=True)
    answer6 = models.TextField(null=True, blank=True)
    step7 = models.CharField(max_length=200,null=True, blank=True)
    answer7 = models.TextField(null=True, blank=True)
    step8 = models.CharField(max_length=200,null=True, blank=True)
    answer8 = models.TextField(null=True, blank=True)
    step9 = models.CharField(max_length=200,null=True, blank=True)
    answer9 = models.TextField(null=True, blank=True)
    step10 = models.CharField(max_length=200,null=True, blank=True)
    answer10 = models.TextField(null=True, blank=True)
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    list15 = models.CharField(max_length=200,blank=True,null=True)
    list16 = models.CharField(max_length=200,blank=True,null=True)
    list17 = models.CharField(max_length=200,blank=True,null=True)
    list18 = models.CharField(max_length=200,blank=True,null=True)
    list19 = models.CharField(max_length=200,blank=True,null=True)
    list20 = models.CharField(max_length=200,blank=True,null=True)
    list21 = models.CharField(max_length=200,blank=True,null=True)
    list22 = models.CharField(max_length=200,blank=True,null=True)
    list23 = models.CharField(max_length=200,blank=True,null=True)
    list24 = models.CharField(max_length=200,blank=True,null=True)
    list25 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category


class FAQ(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    heading_text = models.CharField(max_length=200,null=True, blank=True)
    heading_text2 = models.CharField(max_length=200,null=True, blank=True)
    question1 = models.CharField(max_length=200,null=True, blank=True)
    answer1 = models.TextField(null=True, blank=True)
    question2 = models.CharField(max_length=200,null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    question3 = models.CharField(max_length=200,null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    question4 = models.CharField(max_length=200,null=True, blank=True)
    answer4 = models.TextField(null=True, blank=True)
    question5 = models.CharField(max_length=200,null=True, blank=True)
    answer5 = models.TextField(null=True, blank=True)
    question6 = models.CharField(max_length=200,null=True, blank=True)
    answer6 = models.TextField(null=True, blank=True)
    question7 = models.CharField(max_length=200,null=True, blank=True)
    answer7 = models.TextField(null=True, blank=True)
    list1 = models.CharField(max_length=200,blank=True,null=True)
    list2 = models.CharField(max_length=200,blank=True,null=True)
    list3 = models.CharField(max_length=200,blank=True,null=True)
    list4 = models.CharField(max_length=200,blank=True,null=True)
    list5 = models.CharField(max_length=200,blank=True,null=True)
    list6 = models.CharField(max_length=200,blank=True,null=True)
    list7 = models.CharField(max_length=200,blank=True,null=True)
    list8 = models.CharField(max_length=200,blank=True,null=True)
    list9 = models.CharField(max_length=200,blank=True,null=True)
    list10 = models.CharField(max_length=200,blank=True,null=True)
    list11 = models.CharField(max_length=200,blank=True,null=True)
    list12 = models.CharField(max_length=200,blank=True,null=True)
    list13 = models.CharField(max_length=200,blank=True,null=True)
    list14 = models.CharField(max_length=200,blank=True,null=True)
    list15 = models.CharField(max_length=200,blank=True,null=True)
    list16 = models.CharField(max_length=200,blank=True,null=True)
    list17 = models.CharField(max_length=200,blank=True,null=True)
    list18 = models.CharField(max_length=200,blank=True,null=True)
    list19 = models.CharField(max_length=200,blank=True,null=True)
    list20 = models.CharField(max_length=200,blank=True,null=True)
    list21 = models.CharField(max_length=200,blank=True,null=True)
    list22 = models.CharField(max_length=200,blank=True,null=True)
    list23 = models.CharField(max_length=200,blank=True,null=True)
    list24 = models.CharField(max_length=200,blank=True,null=True)
    list25 = models.CharField(max_length=200,blank=True,null=True)
    list26 = models.CharField(max_length=200,blank=True,null=True)
    list27 = models.CharField(max_length=200,blank=True,null=True)
    list28 = models.CharField(max_length=200,blank=True,null=True)
    list29 = models.CharField(max_length=200,blank=True,null=True)
    list30 = models.CharField(max_length=200,blank=True,null=True)
    list31 = models.CharField(max_length=200,blank=True,null=True)
    list32 = models.CharField(max_length=200,blank=True,null=True)
    list33 = models.CharField(max_length=200,blank=True,null=True)
    list34 = models.CharField(max_length=200,blank=True,null=True)
    list35 = models.CharField(max_length=200,blank=True,null=True)
    list36 = models.CharField(max_length=200,blank=True,null=True)
    list37 = models.CharField(max_length=200,blank=True,null=True)
    list38 = models.CharField(max_length=200,blank=True,null=True)
    list39 = models.CharField(max_length=200,blank=True,null=True)
    list40 = models.CharField(max_length=200,blank=True,null=True)
    list41 = models.CharField(max_length=200,blank=True,null=True)
    list42 = models.CharField(max_length=200,blank=True,null=True)
    list43 = models.CharField(max_length=200,blank=True,null=True)
    list44 = models.CharField(max_length=200,blank=True,null=True)
    list45 = models.CharField(max_length=200,blank=True,null=True)
    list46 = models.CharField(max_length=200,blank=True,null=True)
    list47 = models.CharField(max_length=200,blank=True,null=True)
    list48 = models.CharField(max_length=200,blank=True,null=True)
    list49 = models.CharField(max_length=200,blank=True,null=True)
    list50 = models.CharField(max_length=200,blank=True,null=True)
    list51 = models.CharField(max_length=200,blank=True,null=True)
    list52 = models.CharField(max_length=200,blank=True,null=True)
    list53 = models.CharField(max_length=200,blank=True,null=True)
    list54 = models.CharField(max_length=200,blank=True,null=True)
    list55 = models.CharField(max_length=200,blank=True,null=True)
    list56 = models.CharField(max_length=200,blank=True,null=True)
    list57 = models.CharField(max_length=200,blank=True,null=True)
    list58 = models.CharField(max_length=200,blank=True,null=True)
    list59 = models.CharField(max_length=200,blank=True,null=True)
    list60 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.category

class PricingSum(models.Model):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=200, null=True,blank=False)
    
    heading_text = models.CharField(max_length=200,null=True, blank=True)

    quantity = models.CharField(max_length=200,null=True, blank=True)
    quantity_value = models.CharField(max_length=200,null=True, blank=True)

    mark_pric = models.CharField(max_length=200,null=True, blank=True)
    mark_pric_value = models.CharField(max_length=200,null=True, blank=True)

    dobiz = models.CharField(max_length=200,null=True, blank=True)
    dobiz_value1 = models.CharField(max_length=200,null=True, blank=True)
    dobiz_value2 = models.CharField(max_length=200,null=True, blank=True)

    gst = models.CharField(max_length=200,null=True, blank=True)
    gst_value = models.CharField(max_length=200,null=True, blank=True)

    yoursave = models.CharField(max_length=200,null=True, blank=True)
    yoursave_value = models.CharField(max_length=200,null=True, blank=True)

    govt = models.CharField(max_length=200,null=True, blank=True)
    govt_value = models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return self.category

