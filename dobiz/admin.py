from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

admin.site.site_header ="Dobiz Dashboard"
class OrderSort(ImportExportModelAdmin):
    list_display = ('user','product','email','status','name','address1','address2','address3','remarks','buy_time','order_time')
    list_filter = ('product','email','status','name','buy_time','order_time')
    ordering=["-id"]
admin.site.register(Order,OrderSort)

class CoupanSort(ImportExportModelAdmin):
    list_display = ('coupan','amount','active')
    list_filter = ('coupan','amount','active')
    ordering=["-id"]
admin.site.register(Coupan,CoupanSort)

class ProductSort(ImportExportModelAdmin):
    list_display = ('category','subcategory','product_name','is_package','market_price','Dobiz_India_Filings','gst_percent','gst','other_cost','price')
    list_filter = ('category',)
    ordering=["product_name"]
admin.site.register(Product,ProductSort)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'fname', 'lname', 'phone','is_staff','is_active','is_verified','refer_by')
    list_filter = ('email', 'fname', 'lname', 'phone','is_staff','is_active','is_verified','refer_by')
    fieldsets = (
    (None, {'fields':('email', 'password')}),
    ('additionalfields',{'fields':('fname', 'lname', 'phone','is_staff','is_active','is_verified','otp','otp_for_forgot_pass','otp_for_mobile','refer_by','groups')}),
)
    add_fieldsets=(
    (None,{
        'classes':('wide',),
        'fields':('email', 'password1','password2','fname', 'lname', 'phone','otp','is_staff','is_active','is_verified','refer_by','groups')}),
)
    search_fields=('email',)
    ordering =('email',)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Page)

admin.site.register(Banner)
admin.site.register(Meaning)
admin.site.register(MinimumRequirement)
admin.site.register(Benefits)
admin.site.register(DocumentRequired)
admin.site.register(IncorporationProcess)
admin.site.register(Compliance)
admin.site.register(Closure)
admin.site.register(StepWiseProcedure)
admin.site.register(FAQ)
admin.site.register(PricingSum)
