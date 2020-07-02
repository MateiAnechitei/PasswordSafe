from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Account
from .forms import AccountForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AccountListView(LoginRequiredMixin, ListView):
	model = Account
	template_name = "accounts/account_list.html"
	context_object_name = "account_list"
	def get_queryset(self):
		return Account.objects.filter(owner_id = self.request.user.id)

class AccountDetailView(LoginRequiredMixin, DetailView):
	model = Account
	template_name = "accounts/account_detail.html"
	def get_queryset(self):
		return Account.objects.filter(owner_id = self.request.user.id)

class AccountCreateView(LoginRequiredMixin, CreateView):
	model = Account
	form_class = AccountForm
	template_name = "accounts/account_create.html"
	def get_initial(self):
    		initial = super().get_initial()
    		initial['owner_id'] = self.request.user.id
    		return initial
	def get_success_url(self):
       	 	return reverse('account-list')

class AccountUpdateView(LoginRequiredMixin, UpdateView):
	model = Account
	form_class = AccountForm
	template_name = "accounts/account_create.html"
	def get_object(self):
		id_=self.kwargs.get("id") 
		obj = get_object_or_404(Account, id = id_)
		if obj.owner_id == self.request.user.id:
			return obj
		else:
			return get_object_or_404(Account, id = 0)
	def get_success_url(self):
		return reverse('account-list')
	

class AccountDeleteView(LoginRequiredMixin, DeleteView):
	model = Account
	template_name = "accounts/account_delete.html"
	def get_object(self):
		id_=self.kwargs.get("id") 
		obj = get_object_or_404(Account, id = id_)
		if obj.owner_id == self.request.user.id:
			return obj
		else:
			return get_object_or_404(Account, id = 0)
	def get_success_url(self):
		return reverse('account-list')