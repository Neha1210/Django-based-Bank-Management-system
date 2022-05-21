from django.db import models

# Create your models here.
class user(models.Model):
	name=models.CharField(max_length=200,null=True)
	email=models.CharField(max_length=200,null=True)
	address=models.CharField(max_length=200,null=True)
	Adhar_no=models.CharField(max_length=12,null=True)


	def __str__(self):
		return self.name

class bankaccount(models.Model):
	username=models.ForeignKey(user,null=True,on_delete=models.SET_NULL)
	curr_balance=models.IntegerField(null=True,default=1000)
	acno=models.IntegerField(null=True)

	types=(
		('Saving','Saving'),
		('current','current'),
		('Fixed','Fixed'),
		)
	actype=models.CharField(max_length=200,null=True,choices=types)

	branches=(
		('Latur','Latur'),
		('Barshi','Barshi'),
		('Pune','Pune'),
		('Nanded','Nanded'),
		('Ausa','Ausa'),
		)
	branch=models.CharField(max_length=200,null=True,choices=branches)

	def __str__(self):
		return str(self.acno)


class transaction(models.Model):
	recivername=models.ForeignKey(user,null=True,on_delete=models.SET_NULL)
	accountno=models.ForeignKey(bankaccount,null=True,on_delete=models.SET_NULL,default='')
	amount=models.IntegerField(null=True)
	datetime=models.DateTimeField(null=True,auto_now_add=True)

	def __str__(self):
		return str(self.recivername)