from django.forms import ModelForm
from .models import*

class CreateUserForm(ModelForm):
    class Meta:
        model=user
        fields='__all__'

class CreateAccountForm(ModelForm):
	class Meta:
		model=bankaccount
		fields='__all__'


class TransactionForm(ModelForm):
	class Meta:
		model=transaction
		fields='__all__'