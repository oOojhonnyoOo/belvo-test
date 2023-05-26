from django.urls import path
from transactions.views import TransactionView

urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionView.as_view(), name='transaction-detail'),
    path('transactions/<str:email>/summary', TransactionView.summary, name='transaction-summary')
]