from django.shortcuts import render,redirect
from .forms import*
from .models import*
# Create your views here.
def home(request):
    users=user.objects.all()
    banks=bankaccount.objects.all()

    totalaccount=users.count()
    homebranch=bankaccount.objects.filter(branch='Latur').count()
    totaltrans=transaction.objects.all().count()
    
    context={'users':users,'banks':banks,'totalaccount':totalaccount,'homebranch':homebranch,'totaltrans':totaltrans}

    return render(request,'accounts/home.html',context)

def createuser(request):
	form=CreateUserForm()

	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context={'form':form}		
	return render(request,'accounts/createuser.html',context)

def createaccount(request):

	form=CreateAccountForm()

	if request.method=='POST':
		form=CreateAccountForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context={'form':form}		
	return render(request,'accounts/createaccount.html',context)

def updateuser(request,pk):
	users=user.objects.get(id=pk)
	print(users.name)
	form=CreateUserForm(instance=users)

	if request.method=='POST':
		form=CreateUserForm(request.POST,instance=users)
		if form.is_valid():
			form.save()
			return redirect('home')

	context={'form':form}

	return render(request,'accounts/createuser.html',context)

def updateaccount(request,pk):
		banks=bankaccount.objects.get(id=pk)
		print(banks.username)
		form=CreateAccountForm(instance=banks)
		if request.method=='POST':
			form=CreateAccountForm(request.POST,instance=banks)
			if form.is_valid():
				form.save()
				return redirect('home')
		context={'form':form}

		return render(request,'accounts/createaccount.html',context)
	

def deleteuser(request,pk):
	
	users=user.objects.get(id=pk)

	if request.method=='POST':
		users.delete()

		return redirect('home')

	context={'users':users}

	return render(request,'accounts/deleteuser.html',context)	

def deleteaccount(request,pk):
	banks=bankaccount.objects.get(id=pk)

	if request.method=='POST':
		banks.delete()

		return redirect('home')
	context={'banks':banks}

	return render(request,'accounts/deleteaccount.html',context)

def accountholder(request,pk):
	banks=bankaccount.objects.get(username=pk)
	trans=transaction.objects.all()

	context={'banks':banks,'trans':trans}
	
	return render(request,'accounts/accountholder.html',context)

def all_accounts(request):
	users=user.objects.all()
	banks=bankaccount.objects.all()

	context={'banks':banks,'users':users}

	return render(request,'accounts/all_accounts.html',context)

def madetransaction(request,pk):
	banks=bankaccount.objects.get(id=pk)
 
	senderbal=banks.curr_balance
	form=TransactionForm()

	if request.method=='POST':
		recname=request.POST.get('recivername')
		amount=request.POST.get('amount')
		rec=bankaccount.objects.get(username=recname)
		recbal=rec.curr_balance
		print(recbal)
		form=TransactionForm(request.POST)
		sender=request.POST.get('')
		if form.is_valid():
			senderbal=int(senderbal)-int(amount)
			bankaccount.objects.filter(id=pk).update(curr_balance=senderbal)
			recbal=int(recbal)+int(amount)
			bankaccount.objects.filter(username=recname).update(curr_balance=recbal)
			form.save()
			return redirect('home')
    

	context={'banks':banks,'form':form}

	return render(request,'accounts/transaction.html',context)
