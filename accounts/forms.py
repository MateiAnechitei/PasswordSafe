from django import forms

from .models import Account

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = [
			'owner_id',
			'site',
			'username',
			'password'
		]
		widgets = {'owner_id': forms.HiddenInput()}