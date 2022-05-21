from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(user)
admin.site.register(bankaccount)
admin.site.register(transaction)

'''
class account(models.Model):
	
	username=models.ForeignKey(user,null=True,on_delete=models.SET_NULL)
	account_no=models.CharField(max_length=12,null=True)

	types=(
        ('Saving','Saving'),
        ('Current','Current'),
        ('Fixed','Fixed'),
		)
	account_type=models.CharField(max_length=200,null=True,choices=types)

	branches=(
        ('Latur','Latur'),
        ('Barshi','Barshi'),
        ('Ausa','Ausa'),
        ('Pune','pune'),
        ('Nanded','Nanded')
		) 

	branch=models.CharField(max_length=200,null=True,choices=branches)

'''