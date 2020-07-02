from django.urls import path
from .views import(
	AccountDetailView,
	AccountListView,
	AccountCreateView,
	AccountUpdateView,
	AccountDeleteView
)

urlpatterns = [
	path('', AccountListView.as_view(),name = 'account-list'),
	path('create/', AccountCreateView.as_view(), name = 'create-account'),
	path('<int:pk>/', AccountDetailView.as_view(),name = 'account-detail'),
	path('<int:id>/update', AccountUpdateView.as_view(), name = 'account-update'),
	path('<int:id>/delete', AccountDeleteView.as_view(), name = 'account-delete'),
] 

